from carol_app_monitor import monitor


def execute_monitor():
    """Execute the CarolApp Monitor."""
    monitor_schema = monitor.create_monitor_schema()

    monitor.start_online_processes(monitor_schema, num_retries=2)


if __name__ == "__main__":
    execute_monitor()
