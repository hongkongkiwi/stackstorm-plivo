# Plivo Integration Pack

Pack which allows integration with [Plivo](https://www.plivo.com/) service.

## Configuration

Copy the example configuration in [plivo.yaml.example](./plivo.yaml.example)
to `/opt/stackstorm/configs/plivo.yaml` and edit as required.

It must contain:

* ``auth_id`` - Your account auth id.
* ``auth_token`` - Your account auth token.

Auth ID and Token can be retrieved on the [Plivo Console](https://console.plivo.com/dashboard/) page.

You can also use dynamic values from the datastore. See the
[docs](https://docs.stackstorm.com/reference/pack_configs.html) for more info.

**Note** : When modifying the configuration in `/opt/stackstorm/configs/` please
           remember to tell StackStorm to load these new values by running
           `st2ctl reload --register-configs`

## Actions

* ``send_sms`` - Action which sends an SMS using Twilio API.
