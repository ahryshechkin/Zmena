from zmena.application.messages.inbound.sql_intake import SQLIntakeInboundMessage


class DeltaCrawlerToSQLIntakeHandoff:
    def __init__(self, dco_message):
        self.dco_message = dco_message

    def __repr__(self):
        return "DeltaCrawlerToSQLIntakeHandoff(messages=dco)"

    def prepare(self):
        return SQLIntakeInboundMessage(
            label=self.dco_message.cmt_id,
            name=self.dco_message.name,
            before=self.dco_message.before,
            after=self.dco_message.after,
        )
