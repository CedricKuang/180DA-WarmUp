import app_subscriber
import app_publisher


def initialize_app_subscriber():
    app_subscriber.app_client_initialize()
    return True

def initialize_app_publisher():
    app_publisher.app_client_initialize()
    return True

def disconnect_app_subscriber():
    app_subscriber.app_disconnect()
    return True

def disconnect_app_publisher():
    app_publisher.app_disconnect()
    return True

def get_imu_distance():
    app_publisher.app_publish_data(1)
    distance = app_subscriber.app_collect_data()
    return distance, True