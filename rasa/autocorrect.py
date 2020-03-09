from rasa.nlu.components import Component
import typing
from typing import Any, Optional, Text, Dict


if typing.TYPE_CHECKING:
    from rasa.nlu.model import Metadata


class SpellChecker(Component):
    """A new component"""

    # Defines what attributes the pipeline component will
    # provide when called. The listed attributes
    # should be set by the component on the message object
    # during test and train, e.g.
    # ```message.set("entities", [...])```
    provides = ['text'] #set as text but shouldn't really have much influence on the component

    # Which attributes on a message are required by this
    # component. e.g. if requires contains "tokens", than a
    # previous component in the pipeline needs to have "tokens"
    # within the above described `provides` property.
    requires = []

    # Defines the default configuration parameters of a component
    # these values can be overwritten in the pipeline configuration
    # of the model. The component should choose sensible defaults
    # and should be able to create reasonable results with the defaults.
    defaults = {}

    # Defines what language(s) this component can handle.
    # This attribute is designed for instance method: `can_handle_language`.
    # Default value is None which means it can handle all languages.
    # This is an important feature for backwards compatibility of components.
    language_list = None

    def __init__(self, component_config=None):
        super(SpellChecker, self).__init__(component_config)

    def train(self, training_data, cfg, **kwargs):

        pass

    def process(self, message, **kwargs):

        from autocorrect import Speller
        spell = Speller(lang='en')
        mesg = message.text #get original message
        text = spell(mesg) #correct the message with autocorrect
        message.text = text #set the corrected message as the message for the next components to process


    def persist(self, file_name: Text, model_dir: Text) -> Optional[Dict[Text, Any]]:
        """Persist this component to disk for future loading."""

        pass

    @classmethod
    def load(
        cls,
        meta: Dict[Text, Any],
        model_dir: Optional[Text] = None,
        model_metadata: Optional["Metadata"] = None,
        cached_component: Optional["Component"] = None,
        **kwargs: Any
    ) -> "Component":
        """Load this component from file."""

        if cached_component:
            return cached_component
        else:
            return cls(meta)
