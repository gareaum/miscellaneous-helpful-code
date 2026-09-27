from dataclasses import dataclass, field
from datetime import datetime
import uuid
from typing import Protocol


@dataclass
class Message:
    """ 
    Represents one piece of information being passed between components. 
    
    The payload contains the application-specific information the publisher 
    wants to send, while the timestamp and ID provide information for 
    identifying and tracking that message. 
    """

    payload: dict
    timestamp: datetime
    id: str = field(
        default_factory=lambda: str(uuid.uuid4())
    )

class Subscriber(Protocol):
    """
    Defines how an object receives information from a Topic.

    A subscriber only needs to provide on_message(). The Topic uses this
    method to deliver each Message without needing to know what the
    subscriber actually does with the information.
    """

    def on_message(self, message: Message) -> None:
        """Receives and processes a Message delivered by a Topic."""

        ...

class Topic:
    """
    Represents a named channel that connects publishers to subscribers.

    Subscribers register with a Topic, and any Message published to that
    Topic is passed to every registered subscriber.
    """

    def __init__(self, name: str):
        """Creates a Topic and initializes the list of objects listening to it."""

        self.name = name
        self.subscribers: list[Subscriber] = []

    def add_subscriber(self, subscriber: Subscriber) -> None:
        """Adds an object to the Topic's subscriber list."""

        self.subscribers.append(subscriber)

    def remove_subscriber(self, subscriber: Subscriber) -> None:
        """Removes an object so it will no longer receive messages from the Topic."""
        self.subscribers.remove(subscriber)

    def publish(self, message: Message) -> None:
        """
        Delivers a Message to every subscriber registered to this Topic.

        The Topic calls each subscriber's on_message() method with the same
        Message. An error from one subscriber is caught so it does not stop
        the message from being sent to the remaining subscribers.
        """
        
        for subscriber in self.subscribers:
            try:
                subscriber.on_message(message)
            except Exception as error:
                print(f"Error in subscriber {subscriber}: {error}")

class LoggingSubscriber:
    """
    Implements a subscriber that displays received messages in the console.

    It receives messages through on_message() and prints the message ID
    and payload instead of performing any other processing.
    """

    def __init__(self, name: str):
        """Creates the subscriber and gives it a name for its console output."""

        self.name = name

    def on_message(self, message: Message) -> None:
        """Prints the contents of a Message when the Topic delivers it."""

        print(
            f"{self.name} received {message.id}: "
            f"{message.payload}"
        )

class Broker:
    """
    Keeps track of the Topics used by the Pub/Sub system.

    The Broker is the entry point for publishing and subscribing. It uses
    topic names to find the correct Topic, so publishers and subscribers
    do not need to create or manage Topic objects themselves.
    """

    def __init__(self):
        """Creates a Broker with no Topics registered yet."""

        self.topics: dict[str, Topic] = {}

    def get_or_create_topic(self, name: str) -> Topic:
        
        """
        Finds the Topic with the requested name or creates it if necessary.

        This ensures that subscribing or publishing to a new topic name
        automatically creates the Topic that will handle the communication.
        """

        if name not in self.topics:
            self.topics[name] = Topic(name)

        return self.topics[name]

    def subscribe(self, topic_name: str, subscriber: Subscriber) -> None:
        """
        Connects a subscriber to a Topic using its name.

        Once subscribed, the object's on_message() method will be called
        whenever a Message is published to that Topic.
        """

        self.get_or_create_topic(topic_name).add_subscriber(subscriber)

    def unsubscribe(self, topic_name: str, subscriber: Subscriber) -> None:
        """
        Disconnects a subscriber from a Topic.

        The subscriber will stop receiving messages from that Topic, while
        other subscribers remain connected.
        """

        topic = self.topics.get(topic_name)

        if topic:
            topic.remove_subscriber(subscriber)

    def publish(self, topic_name: str, message: Message,) -> None:
        """
        Sends a Message to a Topic using its name.

        The Broker finds the appropriate Topic and gives it the Message.
        The Topic is then responsible for delivering that Message to every
        subscriber listening to it.
        """

        self.get_or_create_topic(topic_name).publish(message)
        
