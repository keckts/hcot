# components/components/gradient_button.py
from django_viewcomponent import component


@component.register("gradient_button")
class GradientButton(component.Component):
    template_name = "components/gradient_button.html"

    def __init__(self, **kwargs):
        self.text = kwargs.get("text", "Button")
        self.href = kwargs.get("href", "#")
        self.gradient_from = kwargs.get("gradient_from", "from-purple-400")
        self.gradient_to = kwargs.get("gradient_to", "to-pink-600")
        self.extra_classes = kwargs.get("extra_classes", "")

    def get_context_data(self):
        return {
            "text": self.text,
            "href": self.href,
            "gradient_from": self.gradient_from,
            "gradient_to": self.gradient_to,
            "extra_classes": self.extra_classes,
        }
