#!/bin/bash
COMMAND="python ${INSTALL_PREFIX}ominicontacto/manage.py"

# run as user OMNIAPP by default
OMNIAPP_USER=${OMNIAPP_USER:-"{{ usuario }}"}
OMNIAPP_GROUP=${OMNIAPP_GROUP:-${OMNIAPP_USER}}

set -e
until psql -h $PGHOST -U $PGUSER -c '\q'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done
>&2 echo "Postgres is up - executing command"
sleep 5

if [ "$1" = "" ]; then
  if [ ! -f /etc/localtime ]; then
    sudo ln -s /usr/share/zoneinfo/$TZ /etc/localtime
  fi
  if ! crontab -l | grep -q 'conversor.sh'; then
  touch /var/spool/cron/crontabs/omnileads
  printenv | sed 's/^\(.*\)$/export \1/g' | sudo tee -a /etc/profile.d/omnileads_envars.sh
  cat > /var/spool/cron/crontabs/omnileads << EOF
SHELL=/bin/bash
0 1 * * * ${INSTALL_PREFIX}bin/conversor.sh 1 0  >> ${INSTALL_PREFIX}log/conversor.log
EOF
  fi
  $COMMAND migrate --noinput
  $COMMAND createsuperuser --noinput --username=admin --email=admin@example.com || true
  $COMMAND shell << EOF
  from ominicontacto_app.models import User
  u = User.objects.get(username='admin')
  u.set_password('${DJANGO_ADMIN_PASS}')
  u.save()
  exit()
EOF
  $COMMAND populate_history
  $COMMAND compilemessages
  echo 'yes' | $COMMAND collectstatic
  $COMMAND collectstatic_js_reverse
  $COMMAND compress --force
  $COMMAND actualizar_configuracion
  psql -U $PGUSER -h $PGHOST -d $PGDATABASE -c '\i {{ install_prefix }}ominicontacto/reportes_app/sql/plpython/replace_insert_queue_log_ominicontacto_queue_log.sql'
  $COMMAND regenerar_asterisk
  sudo /usr/sbin/crond -l 0 -L /opt/omnileads/log/crond.log
  sudo chown -R omnileads. ${INSTALL_PREFIX}
  echo "Iniciando Django Server"
else
  COMMAND="$@"
fi
{% if devenv == 1 %}
exec $COMMAND runserver 0.0.0.0:1210
{% else %}
exec /usr/bin/uwsgi --ini {{ install_prefix }}run/oml_uwsgi.ini
{% endif %}
