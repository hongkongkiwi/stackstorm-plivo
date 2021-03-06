import plivo

from st2common.runners.base_action import Action

class PlivoSendSMSAction(Action):
    def __init__(self, config):
        super(PlivoSendSMSAction, self).__init__(config=config)
        self.client = plivo.RestClient(auth_id=self.config['auth_id'],
                                       auth_token=self.config['auth_token'])

    def run(self, from_number, to_number, text):
        try:
            self.client.messages.create(text=text, src=from_number, dst=to_number)
        except Exception as e:
            error_msg = ('Failed sending sms to: %s, exception: %s\n' %
                         (to_number, str(e.msg)))
            self.logger.error(error_msg)
            raise Exception(error_msg)

        self.logger.info('Successfully sent sms to: %s\n' % (to_number))
