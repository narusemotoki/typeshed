## Stubs for logging (Python 3.4)

from typing import (
    Any, Callable, Iterable, Mapping, MutableMapping, Optional, IO, Tuple,
    Union,
    overload,
)
from types import TracebackType
import sys

_SysExcInfoType = Union[Tuple[type, BaseException, TracebackType],
                        Tuple[None, None, None]]
if sys.version_info >= (3, 5):
    _ExcInfoType = Union[bool, _SysExcInfoType, Exception]
else:
    _ExcInfoType = Union[bool, _SysExcInfoType]
_ArgsType = Union[Tuple[Any, ...], Dict[str, Any]]
_FilterType = Union['Filter', Callable[[LogRecord], int]]


class Logger:
    propagate = ...  # type: bool
    def setLevel(self, lvl: Union[int, str]) -> None: ...
    def isEnabledFor(self, lvl: int) -> None: ...
    def getEffectiveLevel(self) -> int: ...
    def getChild(self, suffix: str) -> 'Logger': ...
    if sys.version_info > (3,):
        def debug(self, msg: str, *args: Any, exc_info: _ExcInfoType = ...,
                  stack_info: bool = ..., extra: Dict[str, Any] = ...,
                  **kwargs: Any) -> None: ...
        def info(self, msg: str, *args: Any, exc_info: _ExcInfoType = ...,
                 stack_info: bool = ..., extra: Dict[str, Any] = ...,
                 **kwargs: Any) -> None: ...
        def warning(self, msg: str, *args: Any, exc_info: _ExcInfoType = ...,
                    stack_info: bool = ..., extra: Dict[str, Any] = ...,
                    **kwargs: Any) -> None: ...
        def warn(self, msg: str, *args: Any, exc_info: _ExcInfoType = ...,
                 stack_info: bool = ..., extra: Dict[str, Any] = ...,
                 **kwargs: Any) -> None: ...
        def error(self, msg: str, *args: Any, exc_info: _ExcInfoType = ...,
                  stack_info: bool = ..., extra: Dict[str, Any] = ...,
                  **kwargs: Any) -> None: ...
        def critical(self, msg: str, *args: Any, exc_info: _ExcInfoType = ...,
                     stack_info: bool = ..., extra: Dict[str, Any] = ...,
                     **kwargs: Any) -> None: ...
        def log(self, msg: str, *args: Any, exc_info: _ExcInfoType = ...,
                stack_info: bool = ..., extra: Dict[str, Any] = ...,
                **kwargs: Any) -> None: ...
        def exception(self, msg: str, *args: Any, exc_info: _ExcInfoType = ...,
                      stack_info: bool = ..., extra: Dict[str, Any] = ...,
                      **kwargs: Any) -> None: ...
    else:
        def debug(self,  # type: ignore
                  msg: str, *args: Any, exc_info: _ExcInfoType = ...,
                  extra: Dict[str, Any] = ..., **kwargs: Any) -> None: ...
        def info(self,  # type: ignore
                 msg: str, *args: Any, exc_info: _ExcInfoType = ...,
                 extra: Dict[str, Any] = ..., **kwargs: Any) -> None: ...
        def warning(self,  # type: ignore
                    msg: str, *args: Any, exc_info: _ExcInfoType = ...,
                    extra: Dict[str, Any] = ..., **kwargs: Any) -> None: ...
        def warn(self,  # type: ignore
                 msg: str, *args: Any, exc_info: _ExcInfoType = ...,
                 extra: Dict[str, Any] = ..., **kwargs: Any) -> None: ...
        def error(self,  # type: ignore
                  msg: str, *args: Any, exc_info: _ExcInfoType = ...,
                  extra: Dict[str, Any] = ..., **kwargs: Any) -> None: ...
        def critical(self,  # type: ignore
                     msg: str, *args: Any, exc_info: _ExcInfoType = ...,
                     extra: Dict[str, Any] = ..., **kwargs: Any) -> None: ...
        def log(self,  # type: ignore
                msg: str, *args: Any, exc_info: _ExcInfoType = ...,
                extra: Dict[str, Any] = ..., **kwargs: Any) -> None: ...
        def exception(self,  # type: ignore
                      msg: str, *args: Any, exc_info: _ExcInfoType = ...,
                      extra: Dict[str, Any] = ..., **kwargs: Any) -> None: ...
    def addFilter(self, filt: _FilterType) -> None: ...
    def removeFilter(self, filt: _FilterType) -> None: ...
    def filter(self, record: 'LogRecord') -> bool: ...
    def addHandler(self, hdlr: 'Handler') -> None: ...
    def removeHandler(self, hdlr: 'Handler') -> None: ...
    if sys.version_info >= (3,):
        def findCaller(self, stack_info: bool = ...) \
                       -> Tuple[str, int, str, Optional[str]]: ...
    else:
        def findCaller(self  # type: ignore
                       ) -> Tuple[str, int, str]: ...
    def handle(self, record: 'LogRecord') -> None: ...
    if sys.version_info >= (3,):
        def makeRecord(self, name: str, lvl: int, fn: str, lno: int, msg: str,
                       args: Mapping[str, Any],
                       exc_info: Optional[_SysExcInfoType],
                       func: Optional[str] = ...,
                       extra: Optional[Mapping[str, Any]] = ...,
                       sinfo: Optional[str] = ...) -> None: ...
    else:
        def makeRecord(self,  # type: ignore
                       name: str, lvl: int, fn: str, lno: int, msg: str,
                       args: Mapping[str, Any],
                       exc_info: Optional[_SysExcInfoType],
                       func: Optional[str] = ...,
                       extra: Optional[Mapping[str, Any]] = ...) -> None: ...
    if sys.version_info >= (3,):
        def hasHandlers(self) -> bool: ...


CRITICAL = ...  # type: int
ERROR = ...  # type: int
WARNING = ...  # type: int
WARN = ...  # type: int
INFO = ...  # type: int
DEBUG = ...  # type: int
NOTSET = ...  # type: int


class Handler:
    def __init__(self, level: int = ...) -> None: ...
    def createLock(self) -> None: ...
    def acquire(self) -> None: ...
    def release(self) -> None: ...
    def setLevel(self, lvl: Union[int, str]) -> None: ...
    def setFormatter(self, form: 'Formatter') -> None: ...
    def addFilter(self, filt: _FilterType) -> None: ...
    def removeFilter(self, filt: _FilterType) -> None: ...
    def filter(self, record: 'LogRecord') -> bool: ...
    def flush(self) -> None: ...
    def close(self) -> None: ...
    def handle(self, record: 'LogRecord') -> None: ...
    def handleError(self, record: 'LogRecord') -> None: ...
    def format(self, record: 'LogRecord') -> None: ...
    def emit(self, record: 'LogRecord') -> None: ...


class Formatter:
    if sys.version_info >= (3,):
        def __init__(self, fmt: Optional[str] = ...,
                     datefmt: Optional[str] =...,
                     style: str = ...) -> None: ...
    else:
        def __init__(self,  # type: ignore
                     fmt: Optional[str] = ...,
                     datefmt: Optional[str] =...) -> None: ...
    def format(self, record: LogRecord) -> str: ...
    def formatTime(self, record: LogRecord, datefmt: str = ...) -> str: ...
    def formatException(self, exc_info: _SysExcInfoType) -> str: ...
    if sys.version_info >= (3,):
        def formatStack(self, stack_info: str) -> str: ...


class Filter:
    def __init__(self, name: str = ...) -> None: ...
    def filter(self, record: LogRecord) -> int: ...


class LogRecord:
    args = ...  # type: _ArgsType
    asctime = ...  # type: str
    created = ...  # type: int
    exc_info = ...  # type: Optional[_SysExcInfoType]
    filename = ...  # type: str
    funcName = ...  # type: str
    levelname = ...  # type: str
    levelno = ...  # type: int
    lineno = ...  # type: int
    module = ...  # type: str
    msecs = ...  # type: int
    message = ...  # type: str
    msg = ...  # type: str
    name = ...  # type: str
    pathname = ...  # type: str
    process = ...  # type: int
    processName = ...  # type: str
    relativeCreated = ...  # type: int
    if sys.version_info >= (3,):
        stack_info = ...  # type: Optional[str]
    thread = ...  # type: int
    threadName = ...  # type: str
    if sys.version_info >= (3,):
        def __init__(self, name: str, level: int, pathname: str, lineno: int,
                     msg: str, args: _ArgsType,
                     exc_info: Optional[_SysExcInfoType],
                     func: Optional[str] = ...,
                     sinfo: Optional[str] = ...) -> None: ...
    else:
        def __init__(self,  # type: ignore
                     name: str, level: int, pathname: str, lineno: int,
                     msg: str, args: _ArgsType,
                     exc_info: Optional[_SysExcInfoType],
                     func: Optional[str] = ...) -> None: ...
    def getMessage(self) -> str: ...


class LoggerAdapter:
    def __init__(self, logger: Logger, extra: Mapping[str, Any]) -> None: ...
    def process(self, msg: str, kwargs: MutableMapping[str, Any]) \
                -> Tuple[str, MutableMapping[str, Any]]: ...
    if sys.version_info > (3,):
        def debug(self, msg: str, *args: Any, exc_info: _ExcInfoType = ...,
                  stack_info: bool = ..., extra: Dict[str, Any] = ...,
                  **kwargs: Any) -> None: ...
        def info(self, msg: str, *args: Any, exc_info: _ExcInfoType = ...,
                 stack_info: bool = ..., extra: Dict[str, Any] = ...,
                 **kwargs: Any) -> None: ...
        def warning(self, msg: str, *args: Any, exc_info: _ExcInfoType = ...,
                    stack_info: bool = ..., extra: Dict[str, Any] = ...,
                    **kwargs: Any) -> None: ...
        def error(self, msg: str, *args: Any, exc_info: _ExcInfoType = ...,
                  stack_info: bool = ..., extra: Dict[str, Any] = ...,
                  **kwargs: Any) -> None: ...
        def exception(self, msg: str, *args: Any, exc_info: _ExcInfoType = ...,
                      stack_info: bool = ..., extra: Dict[str, Any] = ...,
                      **kwargs: Any) -> None: ...
        def critical(self, msg: str, *args: Any, exc_info: _ExcInfoType = ...,
                     stack_info: bool = ..., extra: Dict[str, Any] = ...,
                     **kwargs: Any) -> None: ...
        def log(self, msg: str, *args: Any, exc_info: _ExcInfoType = ...,
                stack_info: bool = ..., extra: Dict[str, Any] = ...,
                **kwargs: Any) -> None: ...
    else:
        def debug(self,  # type: ignore
                  msg: str, *args: Any, exc_info: _ExcInfoType = ...,
                  extra: Dict[str, Any] = ..., **kwargs: Any) -> None: ...
        def info(self,  # type: ignore
                 msg: str, *args: Any, exc_info: _ExcInfoType = ...,
                 extra: Dict[str, Any] = ..., **kwargs: Any) -> None: ...
        def warning(self,  # type: ignore
                    msg: str, *args: Any, exc_info: _ExcInfoType = ...,
                    extra: Dict[str, Any] = ..., **kwargs: Any) -> None: ...
        def error(self,  # type: ignore
                  msg: str, *args: Any, exc_info: _ExcInfoType = ...,
                  extra: Dict[str, Any] = ..., **kwargs: Any) -> None: ...
        def exception(self,  # type: ignore
                      msg: str, *args: Any, exc_info: _ExcInfoType = ...,
                      extra: Dict[str, Any] = ..., **kwargs: Any) -> None: ...
        def critical(self,  # type: ignore
                     msg: str, *args: Any, exc_info: _ExcInfoType = ...,
                     extra: Dict[str, Any] = ..., **kwargs: Any) -> None: ...
        def log(self,  # type: ignore
                msg: str, *args: Any, exc_info: _ExcInfoType = ...,
                extra: Dict[str, Any] = ..., **kwargs: Any) -> None: ...
    def isEnabledFor(self, lvl: int) -> None: ...
    if sys.version_info >= (3,):
        def getEffectiveLevel(self) -> int: ...
        def setLevel(self, lvl: Union[int, str]) -> None: ...
        def hasHandlers(self) -> bool: ...


# TODO uncomment when mypy handle conditionals
#if sys.version_info >= (3,):
#    def getLogger(name: Optional[str] = ...) -> Logger: ...
#else:
#    @overload
#    def getLogger() -> Logger: ...
#    @overload
#    def getLogger(name: str) -> Logger: ...
def getLogger(name: Optional[str] = ...) -> Logger: ...
def getLoggerClass() -> type: ...
if sys.version_info >= (3,):
    def getLogRecordFactory() -> Callable[..., LogRecord]: ...

if sys.version_info > (3,):
    def debug(msg: str, *args: Any, exc_info: _ExcInfoType = ...,
              stack_info: bool = ..., extra: Dict[str, Any] = ...,
              **kwargs: Any) -> None: ...
    def info(msg: str, *args: Any, exc_info: _ExcInfoType = ...,
             stack_info: bool = ..., extra: Dict[str, Any] = ...,
             **kwargs: Any) -> None: ...
    def warning(msg: str, *args: Any, exc_info: _ExcInfoType = ...,
                stack_info: bool = ..., extra: Dict[str, Any] = ...,
                **kwargs: Any) -> None: ...
    def warn(msg: str, *args: Any, exc_info: _ExcInfoType = ...,
             stack_info: bool = ..., extra: Dict[str, Any] = ...,
             **kwargs: Any) -> None: ...
    def error(msg: str, *args: Any, exc_info: _ExcInfoType = ...,
              stack_info: bool = ..., extra: Dict[str, Any] = ...,
              **kwargs: Any) -> None: ...
    def critical(msg: str, *args: Any, exc_info: _ExcInfoType = ...,
                 stack_info: bool = ..., extra: Dict[str, Any] = ...,
                 **kwargs: Any) -> None: ...
    def exception(msg: str, *args: Any, exc_info: _ExcInfoType = ...,
                  stack_info: bool = ..., extra: Dict[str, Any] = ...,
                  **kwargs: Any) -> None: ...
    def log(msg: str, *args: Any, exc_info: _ExcInfoType = ...,
            stack_info: bool = ..., extra: Dict[str, Any] = ...,
            **kwargs: Any) -> None: ...
else:
    def debug(# type: ignore
              msg: str, *args: Any, exc_info: _ExcInfoType = ...,
              extra: Dict[str, Any] = ..., **kwargs: Any) -> None: ...
    def info(# type: ignore
             msg: str, *args: Any, exc_info: _ExcInfoType = ...,
             extra: Dict[str, Any] = ..., **kwargs: Any) -> None: ...
    def warning(# type: ignore
                msg: str, *args: Any, exc_info: _ExcInfoType = ...,
                extra: Dict[str, Any] = ..., **kwargs: Any) -> None: ...
    def warn(# type: ignore
             msg: str, *args: Any, exc_info: _ExcInfoType = ...,
             extra: Dict[str, Any] = ..., **kwargs: Any) -> None: ...
    def error(# type: ignore
              msg: str, *args: Any, exc_info: _ExcInfoType = ...,
              extra: Dict[str, Any] = ..., **kwargs: Any) -> None: ...
    def critical(# type: ignore
                 msg: str, *args: Any, exc_info: _ExcInfoType = ...,
                 extra: Dict[str, Any] = ..., **kwargs: Any) -> None: ...
    def exception(# type: ignore
                  msg: str, *args: Any, exc_info: _ExcInfoType = ...,
                  extra: Dict[str, Any] = ..., **kwargs: Any) -> None: ...
    def log(# type: ignore
            msg: str, *args: Any, exc_info: _ExcInfoType = ...,
            extra: Dict[str, Any] = ..., **kwargs: Any) -> None: ...

def disable(lvl: int) -> None: ...
def addLevelName(lvl: int, levelName: str) -> None: ...
def getLevelName(lvl: int) -> str: ...

def makeLogRecord(attrdict: Mapping[str, Any]) -> LogRecord: ...

# TODO uncomment when mypy handle conditionals
#if sys.version_info >= (3,):
#    def basicConfig(*, filename: str = ..., filemode: str = ...,
#                    format: str = ..., datefmt: str = ..., style: str = ...,
#                    level: int = ..., stream: IO[str] = ...,
#                    handlers: Iterable[Handler]) -> None: ...
#else:
#    @overload
#    def basicConfig() -> None: ...
#    @overload
#    def basicConfig(*, filename: str = ..., filemode: str = ...,
#                    format: str = ..., datefmt: str = ...,
#                    level: int = ..., stream: IO[str] = ...) -> None: ...
def basicConfig(*, filename: str = ..., filemode: str = ...,
                format: str = ..., datefmt: str = ..., style: str = ...,
                level: int = ..., stream: IO[str] = ...,
                handlers: Iterable[Handler]) -> None: ...
def shutdown() -> None: ...

def setLoggerClass(klass: type) -> None: ...
if sys.version_info >= (3,):
    def setLogRecordFactory(factory: Callable[..., LogRecord]) -> None: ...


if sys.version_info >= (3,):
    lastResort = ...  # type: Optional['StreamHandler']


class StreamHandler(Handler):
    def __init__(self, stream: Optional[IO[str]] = ...) -> None: ...


class FileHandler(Handler):
    def __init__(self, filename: str, mode: str = ...,
                 encoding: Optional[str] = ..., delay: bool = ...) -> None: ...


class NullHandler(Handler): ...
