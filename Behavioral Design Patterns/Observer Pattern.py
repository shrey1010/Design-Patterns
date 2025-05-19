class Subscriber:
    def notify(self, video_title):
        pass

class User(Subscriber):
    def __init__(self, name):
        self.name = name

    def notify(self, video_title):
        print(f"{self.name} got notified: New video uploaded - {video_title}")


class YouTubeChannel:
    def __init__(self, channel_name):
        self.channel_name = channel_name
        self.subscribers = []

    def subscribe(self, user):
        self.subscribers.append(user)
        print(f"{user.name} subscribed to {self.channel_name}")

    def unsubscribe(self, user):
        self.subscribers.remove(user)
        print(f"{user.name} unsubscribed from {self.channel_name}")

    def upload_video(self, title):
        print(f"\n{self.channel_name} uploaded a new video: {title}")
        self.notify_subscribers(title)

    def notify_subscribers(self, video_title):
        for subscriber in self.subscribers:
            subscriber.notify(video_title)


# Create a channel (Publisher)
channel = YouTubeChannel("CodeWithAI")

# Create users (Subscribers)
alice = User("Alice")
bob = User("Bob")

# Subscribe users to the channel
channel.subscribe(alice)
channel.subscribe(bob)

# Upload a new video
channel.upload_video("Observer Pattern Explained")

# Unsubscribe one user and upload another video
channel.unsubscribe(bob)
channel.upload_video("Decorator Pattern in Python")
