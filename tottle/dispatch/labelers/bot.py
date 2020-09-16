from tottle.dispatch.handlers import FunctionHandler
from tottle.dispatch.labelers.abc import ABCBotLabeler, LabeledMessageHandler
from tottle.dispatch.rules import ABCRule
from tottle.dispatch.rules.message import FromChatRule, PrivateMessageRule
from tottle.dispatch.views import MessageView


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

    def private_message(
            self, *rules: "ABCRule", **custom_rules
    ) -> LabeledMessageHandler:
        def decorator(func):
            self.message_view.handlers.append(
                FunctionHandler(
                    func, PrivateMessageRule(),
                    *rules, *self.get_custom_rules(custom_rules),
                )
            )
            return func

        return decorator

