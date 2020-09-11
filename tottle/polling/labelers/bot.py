from tottle.polling.handlers.function import FunctionHandler
from tottle.polling.labelers.abc import ABCBotLabeler, LabeledMessageHandler
from tottle.polling.rules import ABCRule
from tottle.polling.rules.message import FromChatRule
from tottle.polling.views import MessageView


class BotLabeler(ABCBotLabeler):
    message_view = MessageView()

    def message(
            self, *rules: "ABCRule", **custom_rules
    ) -> LabeledMessageHandler:
        def decorator(func):
            self.message_view.handlers.append(
                FunctionHandler(
                    func, *rules, *self.get_custom_rules(custom_rules),
                )
            )
            return func

        return decorator

    def chat_message(
            self, *rules: "ABCRule", **custom_rules
    ) -> LabeledMessageHandler:
        def decorator(func):
            self.message_view.handlers.append(
                FunctionHandler(
                    func, FromChatRule(),
                    *rules, *self.get_custom_rules(custom_rules),
                )
            )
            return func

        return decorator
