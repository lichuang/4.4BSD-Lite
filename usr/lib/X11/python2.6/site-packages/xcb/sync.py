#
# This file generated automatically from sync.xml by py_client.py.
# Edit at your peril.
#

import xcb
import cStringIO
from struct import pack, unpack_from
from array import array
import xproto

MAJOR_VERSION = 3
MINOR_VERSION = 1

key = xcb.ExtensionKey('SYNC')

class ALARMSTATE:
    Active = 0
    Inactive = 1
    Destroyed = 2

class TESTTYPE:
    PositiveTransition = 0
    NegativeTransition = 1
    PositiveComparison = 2
    NegativeComparison = 3

class VALUETYPE:
    Absolute = 0
    Relative = 1

class CA:
    Counter = 1
    ValueType = 2
    Value = 4
    TestType = 8
    Delta = 16
    Events = 32

class INT64(xcb.Struct):
    def __init__(self, parent, offset, size):
        xcb.Struct.__init__(self, parent, offset, size)
        (self.hi, self.lo,) = unpack_from('iI', parent, offset)

class SYSTEMCOUNTER(xcb.Struct):
    def __init__(self, parent, offset):
        xcb.Struct.__init__(self, parent, offset)
        base = offset
        (self.counter,) = unpack_from('I', parent, offset)
        offset += 4
        self.resolution = INT64(parent, offset, 8)
        offset += 8
        (self.name_len,) = unpack_from('H', parent, offset)
        offset += 2
        offset += xcb.type_pad(1, offset)
        self.name = xcb.List(parent, offset, self.name_len, 'b', 1)
        offset += len(self.name.buf())
        xcb._resize_obj(self, offset - base)

class TRIGGER(xcb.Struct):
    def __init__(self, parent, offset, size):
        xcb.Struct.__init__(self, parent, offset, size)
        (self.counter, self.wait_type,) = unpack_from('II', parent, offset)
        offset += 8
        self.wait_value = INT64(parent, offset, 8)
        offset += 8
        offset += xcb.type_pad(4, offset)
        (self.test_type,) = unpack_from('I', parent, offset)

class WAITCONDITION(xcb.Struct):
    def __init__(self, parent, offset, size):
        xcb.Struct.__init__(self, parent, offset, size)
        self.trigger = TRIGGER(parent, offset, 20)
        offset += 20
        offset += xcb.type_pad(8, offset)
        self.event_threshold = INT64(parent, offset, 8)

class CounterError(xcb.Error):
    def __init__(self, parent, offset=0):
        xcb.Error.__init__(self, parent, offset)
        (self.bad_counter, self.minor_opcode, self.major_opcode,) = unpack_from('xx2xIHB', parent, offset)

class BadCounter(xcb.ProtocolException):
    pass

class AlarmError(xcb.Error):
    def __init__(self, parent, offset=0):
        xcb.Error.__init__(self, parent, offset)
        (self.bad_alarm, self.minor_opcode, self.major_opcode,) = unpack_from('xx2xIHB', parent, offset)

class BadAlarm(xcb.ProtocolException):
    pass

class InitializeCookie(xcb.Cookie):
    pass

class InitializeReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        (self.major_version, self.minor_version,) = unpack_from('xx2x4xBB22x', parent, offset)

class ListSystemCountersCookie(xcb.Cookie):
    pass

class ListSystemCountersReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        (self.counters_len,) = unpack_from('xx2x4xI20x', parent, offset)
        offset += 32
        self.counters = xcb.List(parent, offset, self.counters_len, SYSTEMCOUNTER, -1)

class QueryCounterCookie(xcb.Cookie):
    pass

class QueryCounterReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        offset += 8
        self.counter_value = INT64(parent, offset, 8)

class QueryAlarmCookie(xcb.Cookie):
    pass

class QueryAlarmReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        offset += 8
        self.trigger = TRIGGER(parent, offset, 20)
        offset += 20
        offset += xcb.type_pad(8, offset)
        self.delta = INT64(parent, offset, 8)
        offset += 8
        offset += xcb.type_pad(4, offset)
        (self.events, self.state,) = unpack_from('BB2x', parent, offset)

class GetPriorityCookie(xcb.Cookie):
    pass

class GetPriorityReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        (self.priority,) = unpack_from('xx2x4xi', parent, offset)

class QueryFenceCookie(xcb.Cookie):
    pass

class QueryFenceReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        (self.triggered,) = unpack_from('xx2x4xB23x', parent, offset)

class CounterNotifyEvent(xcb.Event):
    def __init__(self, parent, offset=0):
        xcb.Event.__init__(self, parent, offset)
        (self.kind, self.counter,) = unpack_from('xB2xI', parent, offset)
        offset += 8
        self.wait_value = INT64(parent, offset, 8)
        offset += 8
        offset += xcb.type_pad(8, offset)
        self.counter_value = INT64(parent, offset, 8)
        offset += 8
        offset += xcb.type_pad(4, offset)
        (self.timestamp, self.count, self.destroyed,) = unpack_from('IHBx', parent, offset)

class AlarmNotifyEvent(xcb.Event):
    def __init__(self, parent, offset=0):
        xcb.Event.__init__(self, parent, offset)
        (self.kind, self.alarm,) = unpack_from('xB2xI', parent, offset)
        offset += 8
        self.counter_value = INT64(parent, offset, 8)
        offset += 8
        offset += xcb.type_pad(8, offset)
        self.alarm_value = INT64(parent, offset, 8)
        offset += 8
        offset += xcb.type_pad(4, offset)
        (self.timestamp, self.state,) = unpack_from('IB3x', parent, offset)

class syncExtension(xcb.Extension):

    def Initialize(self, desired_major_version, desired_minor_version):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xBB', desired_major_version, desired_minor_version))
        return self.send_request(xcb.Request(buf.getvalue(), 0, False, True),
                                 InitializeCookie(),
                                 InitializeReply)

    def InitializeUnchecked(self, desired_major_version, desired_minor_version):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xBB', desired_major_version, desired_minor_version))
        return self.send_request(xcb.Request(buf.getvalue(), 0, False, False),
                                 InitializeCookie(),
                                 InitializeReply)

    def ListSystemCounters(self, ):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2x', ))
        return self.send_request(xcb.Request(buf.getvalue(), 1, False, True),
                                 ListSystemCountersCookie(),
                                 ListSystemCountersReply)

    def ListSystemCountersUnchecked(self, ):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2x', ))
        return self.send_request(xcb.Request(buf.getvalue(), 1, False, False),
                                 ListSystemCountersCookie(),
                                 ListSystemCountersReply)

    def CreateCounterChecked(self, id, initial_value):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', id))
        for elt in xcb.Iterator(initial_value, 2, 'initial_value', False):
            buf.write(pack('=iI', *elt))
        return self.send_request(xcb.Request(buf.getvalue(), 2, True, True),
                                 xcb.VoidCookie())

    def CreateCounter(self, id, initial_value):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', id))
        for elt in xcb.Iterator(initial_value, 2, 'initial_value', False):
            buf.write(pack('=iI', *elt))
        return self.send_request(xcb.Request(buf.getvalue(), 2, True, False),
                                 xcb.VoidCookie())

    def DestroyCounterChecked(self, counter):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', counter))
        return self.send_request(xcb.Request(buf.getvalue(), 6, True, True),
                                 xcb.VoidCookie())

    def DestroyCounter(self, counter):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', counter))
        return self.send_request(xcb.Request(buf.getvalue(), 6, True, False),
                                 xcb.VoidCookie())

    def QueryCounter(self, counter):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', counter))
        return self.send_request(xcb.Request(buf.getvalue(), 5, False, True),
                                 QueryCounterCookie(),
                                 QueryCounterReply)

    def QueryCounterUnchecked(self, counter):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', counter))
        return self.send_request(xcb.Request(buf.getvalue(), 5, False, False),
                                 QueryCounterCookie(),
                                 QueryCounterReply)

    def AwaitChecked(self, wait_list_len, wait_list):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2x', ))
        for elt in xcb.Iterator(wait_list, 7, 'wait_list', True):
            buf.write(pack('=IIiIIiI', *elt))
        return self.send_request(xcb.Request(buf.getvalue(), 7, True, True),
                                 xcb.VoidCookie())

    def Await(self, wait_list_len, wait_list):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2x', ))
        for elt in xcb.Iterator(wait_list, 7, 'wait_list', True):
            buf.write(pack('=IIiIIiI', *elt))
        return self.send_request(xcb.Request(buf.getvalue(), 7, True, False),
                                 xcb.VoidCookie())

    def ChangeCounterChecked(self, counter, amount):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', counter))
        for elt in xcb.Iterator(amount, 2, 'amount', False):
            buf.write(pack('=iI', *elt))
        return self.send_request(xcb.Request(buf.getvalue(), 4, True, True),
                                 xcb.VoidCookie())

    def ChangeCounter(self, counter, amount):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', counter))
        for elt in xcb.Iterator(amount, 2, 'amount', False):
            buf.write(pack('=iI', *elt))
        return self.send_request(xcb.Request(buf.getvalue(), 4, True, False),
                                 xcb.VoidCookie())

    def SetCounterChecked(self, counter, value):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', counter))
        for elt in xcb.Iterator(value, 2, 'value', False):
            buf.write(pack('=iI', *elt))
        return self.send_request(xcb.Request(buf.getvalue(), 3, True, True),
                                 xcb.VoidCookie())

    def SetCounter(self, counter, value):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', counter))
        for elt in xcb.Iterator(value, 2, 'value', False):
            buf.write(pack('=iI', *elt))
        return self.send_request(xcb.Request(buf.getvalue(), 3, True, False),
                                 xcb.VoidCookie())

    def CreateAlarmChecked(self, id, value_mask, value_list):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xII', id, value_mask))
        for elt in xcb.Iterator(value_list, 8, 'value_list', False):
            buf.write(pack('=IIiIIiII', *elt))
        return self.send_request(xcb.Request(buf.getvalue(), 8, True, True),
                                 xcb.VoidCookie())

    def CreateAlarm(self, id, value_mask, value_list):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xII', id, value_mask))
        for elt in xcb.Iterator(value_list, 8, 'value_list', False):
            buf.write(pack('=IIiIIiII', *elt))
        return self.send_request(xcb.Request(buf.getvalue(), 8, True, False),
                                 xcb.VoidCookie())

    def ChangeAlarmChecked(self, id, value_mask, value_list):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xII', id, value_mask))
        for elt in xcb.Iterator(value_list, 8, 'value_list', False):
            buf.write(pack('=IIiIIiII', *elt))
        return self.send_request(xcb.Request(buf.getvalue(), 9, True, True),
                                 xcb.VoidCookie())

    def ChangeAlarm(self, id, value_mask, value_list):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xII', id, value_mask))
        for elt in xcb.Iterator(value_list, 8, 'value_list', False):
            buf.write(pack('=IIiIIiII', *elt))
        return self.send_request(xcb.Request(buf.getvalue(), 9, True, False),
                                 xcb.VoidCookie())

    def DestroyAlarmChecked(self, alarm):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', alarm))
        return self.send_request(xcb.Request(buf.getvalue(), 11, True, True),
                                 xcb.VoidCookie())

    def DestroyAlarm(self, alarm):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', alarm))
        return self.send_request(xcb.Request(buf.getvalue(), 11, True, False),
                                 xcb.VoidCookie())

    def QueryAlarm(self, alarm):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', alarm))
        return self.send_request(xcb.Request(buf.getvalue(), 10, False, True),
                                 QueryAlarmCookie(),
                                 QueryAlarmReply)

    def QueryAlarmUnchecked(self, alarm):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', alarm))
        return self.send_request(xcb.Request(buf.getvalue(), 10, False, False),
                                 QueryAlarmCookie(),
                                 QueryAlarmReply)

    def SetPriorityChecked(self, id, priority):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIi', id, priority))
        return self.send_request(xcb.Request(buf.getvalue(), 12, True, True),
                                 xcb.VoidCookie())

    def SetPriority(self, id, priority):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIi', id, priority))
        return self.send_request(xcb.Request(buf.getvalue(), 12, True, False),
                                 xcb.VoidCookie())

    def GetPriority(self, id):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', id))
        return self.send_request(xcb.Request(buf.getvalue(), 13, False, True),
                                 GetPriorityCookie(),
                                 GetPriorityReply)

    def GetPriorityUnchecked(self, id):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', id))
        return self.send_request(xcb.Request(buf.getvalue(), 13, False, False),
                                 GetPriorityCookie(),
                                 GetPriorityReply)

    def CreateFenceChecked(self, drawable, fence, initially_triggered):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIIB', drawable, fence, initially_triggered))
        return self.send_request(xcb.Request(buf.getvalue(), 14, True, True),
                                 xcb.VoidCookie())

    def CreateFence(self, drawable, fence, initially_triggered):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIIB', drawable, fence, initially_triggered))
        return self.send_request(xcb.Request(buf.getvalue(), 14, True, False),
                                 xcb.VoidCookie())

    def TriggerFenceChecked(self, fence):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', fence))
        return self.send_request(xcb.Request(buf.getvalue(), 15, True, True),
                                 xcb.VoidCookie())

    def TriggerFence(self, fence):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', fence))
        return self.send_request(xcb.Request(buf.getvalue(), 15, True, False),
                                 xcb.VoidCookie())

    def ResetFenceChecked(self, fence):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', fence))
        return self.send_request(xcb.Request(buf.getvalue(), 16, True, True),
                                 xcb.VoidCookie())

    def ResetFence(self, fence):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', fence))
        return self.send_request(xcb.Request(buf.getvalue(), 16, True, False),
                                 xcb.VoidCookie())

    def DestroyFenceChecked(self, fence):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', fence))
        return self.send_request(xcb.Request(buf.getvalue(), 17, True, True),
                                 xcb.VoidCookie())

    def DestroyFence(self, fence):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', fence))
        return self.send_request(xcb.Request(buf.getvalue(), 17, True, False),
                                 xcb.VoidCookie())

    def QueryFence(self, fence):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', fence))
        return self.send_request(xcb.Request(buf.getvalue(), 18, False, True),
                                 QueryFenceCookie(),
                                 QueryFenceReply)

    def QueryFenceUnchecked(self, fence):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', fence))
        return self.send_request(xcb.Request(buf.getvalue(), 18, False, False),
                                 QueryFenceCookie(),
                                 QueryFenceReply)

    def AwaitFenceChecked(self, fence_list_len, fence_list):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2x', ))
        buf.write(str(buffer(array('I', fence_list))))
        return self.send_request(xcb.Request(buf.getvalue(), 19, True, True),
                                 xcb.VoidCookie())

    def AwaitFence(self, fence_list_len, fence_list):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2x', ))
        buf.write(str(buffer(array('I', fence_list))))
        return self.send_request(xcb.Request(buf.getvalue(), 19, True, False),
                                 xcb.VoidCookie())

_events = {
    0 : CounterNotifyEvent,
    1 : AlarmNotifyEvent,
}

_errors = {
    0 : (CounterError, BadCounter),
    1 : (AlarmError, BadAlarm),
}

xcb._add_ext(key, syncExtension, _events, _errors)
