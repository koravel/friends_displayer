import traceback


class _LogLevel:
    OFF = 0
    FATAL = 1
    CRITICAL = 2
    ERROR = 3
    WARN = 4
    INFO = 5
    DEBUG = 6
    TRACE = 7

    title = {
        TRACE: "TRACE",
        DEBUG: "DEBUG",
        INFO: "INFO",
        WARN: "WARNING",
        ERROR: "ERROR",
        CRITICAL: "CRITICAL",
        FATAL: "FATAL"
    }


def print_log(text):
    print("{}\n{}".format(traceback.format_exc(), text))