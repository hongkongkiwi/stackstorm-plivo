import plivo

from st2common.runners.base_action import Action

class PlivoMakeCallAction(Action):
    def __init__(self, config):
        super(PlivoMakeCallAction, self).__init__(config=config)
        self.client = plivo.RestClient(auth_id=self.config['auth_id'],
                                       auth_token=self.config['auth_token'])

    def run(self, from_number, to_number, answer_url):
        try:
            self.client.calls.create(answer_url=answer_url, from_=from_number, to_=to_number)
        except Exception as e:
            error_msg = ('Failed making a call to: %s, exception: %s\n' %
                         (to_number, str(e.msg)))
            self.logger.error(error_msg)
            raise Exception(error_msg)

        self.logger.info('Successfully make call to: %s\n' % (to_number))
