#
# This file generated automatically from xv.xml by py_client.py.
# Edit at your peril.
#

import xcb
import cStringIO
from struct import pack, unpack_from
from array import array
import xproto
import shm

MAJOR_VERSION = 2
MINOR_VERSION = 2

key = xcb.ExtensionKey('XVideo')

class Type:
    InputMask = 1
    OutputMask = 2
    VideoMask = 4
    StillMask = 8
    ImageMask = 16

class ImageFormatInfoType:
    RGB = 0
    YUV = 1

class ImageFormatInfoFormat:
    Packed = 0
    Planar = 1

class AttributeFlag:
    Gettable = 1
    Settable = 2

class VideoNotifyReason:
    Started = 0
    Stopped = 1
    Busy = 2
    Preempted = 3
    HardError = 4

class ScanlineOrder:
    TopToBottom = 0
    BottomToTop = 1

class GrabPortStatus:
    Success = 0
    BadExtension = 1
    AlreadyGrabbed = 2
    InvalidTime = 3
    BadReply = 4
    BadAlloc = 5

class Rational(xcb.Struct):
    def __init__(self, parent, offset, size):
        xcb.Struct.__init__(self, parent, offset, size)
        (self.numerator, self.denominator,) = unpack_from('ii', parent, offset)

class Format(xcb.Struct):
    def __init__(self, parent, offset, size):
        xcb.Struct.__init__(self, parent, offset, size)
        (self.visual, self.depth,) = unpack_from('IB3x', parent, offset)

class AdaptorInfo(xcb.Struct):
    def __init__(self, parent, offset):
        xcb.Struct.__init__(self, parent, offset)
        base = offset
        (self.base_id, self.name_size, self.num_ports, self.num_formats, self.type,) = unpack_from('IHHHBx', parent, offset)
        offset += 12
        self.name = xcb.List(parent, offset, self.name_size, 'b', 1)
        offset += len(self.name.buf())
        offset += 1
        offset += xcb.type_pad(8, offset)
        self.formats = xcb.List(parent, offset, self.num_formats, Format, 8)
        offset += len(self.formats.buf())
        xcb._resize_obj(self, offset - base)

class EncodingInfo(xcb.Struct):
    def __init__(self, parent, offset):
        xcb.Struct.__init__(self, parent, offset)
        base = offset
        (self.encoding, self.name_size, self.width, self.height,) = unpack_from('IHHH2x', parent, offset)
        offset += 12
        self.rate = Rational(parent, offset, 8)
        offset += 8
        offset += xcb.type_pad(1, offset)
        self.name = xcb.List(parent, offset, self.name_size, 'b', 1)
        offset += len(self.name.buf())
        xcb._resize_obj(self, offset - base)

class Image(xcb.Struct):
    def __init__(self, parent, offset):
        xcb.Struct.__init__(self, parent, offset)
        base = offset
        (self.id, self.width, self.height, self.data_size, self.num_planes,) = unpack_from('IHHII', parent, offset)
        offset += 16
        self.pitches = xcb.List(parent, offset, self.num_planes, 'I', 4)
        offset += len(self.pitches.buf())
        offset += xcb.type_pad(4, offset)
        self.offsets = xcb.List(parent, offset, self.num_planes, 'I', 4)
        offset += len(self.offsets.buf())
        offset += xcb.type_pad(1, offset)
        self.data = xcb.List(parent, offset, self.data_size, 'B', 1)
        offset += len(self.data.buf())
        xcb._resize_obj(self, offset - base)

class AttributeInfo(xcb.Struct):
    def __init__(self, parent, offset):
        xcb.Struct.__init__(self, parent, offset)
        base = offset
        (self.flags, self.min, self.max, self.size,) = unpack_from('IiiI', parent, offset)
        offset += 16
        self.name = xcb.List(parent, offset, self.size, 'b', 1)
        offset += len(self.name.buf())
        xcb._resize_obj(self, offset - base)

class ImageFormatInfo(xcb.Struct):
    def __init__(self, parent, offset, size):
        xcb.Struct.__init__(self, parent, offset, size)
        (self.id, self.type, self.byte_order,) = unpack_from('IBB2x', parent, offset)
        offset += 8
        self.guid = xcb.List(parent, offset, 16, 'B', 1)
        offset += len(self.guid.buf())
        (self.bpp, self.num_planes, self.depth, self.red_mask, self.green_mask, self.blue_mask, self.format, self.y_sample_bits, self.u_sample_bits, self.v_sample_bits, self.vhorz_y_period, self.vhorz_u_period, self.vhorz_v_period, self.vvert_y_period, self.vvert_u_period, self.vvert_v_period,) = unpack_from('BB2xB3xIIIB3xIIIIIIIII', parent, offset)
        offset += 60
        offset += xcb.type_pad(1, offset)
        self.vcomp_order = xcb.List(parent, offset, 32, 'B', 1)
        offset += len(self.vcomp_order.buf())
        offset += xcb.type_pad(4, offset)
        (self.vscanline_order,) = unpack_from('B11x', parent, offset)

class PortError(xcb.Error):
    def __init__(self, parent, offset=0):
        xcb.Error.__init__(self, parent, offset)

class BadPort(xcb.ProtocolException):
    pass

class EncodingError(xcb.Error):
    def __init__(self, parent, offset=0):
        xcb.Error.__init__(self, parent, offset)

class BadEncoding(xcb.ProtocolException):
    pass

class ControlError(xcb.Error):
    def __init__(self, parent, offset=0):
        xcb.Error.__init__(self, parent, offset)

class BadControl(xcb.ProtocolException):
    pass

class VideoNotifyEvent(xcb.Event):
    def __init__(self, parent, offset=0):
        xcb.Event.__init__(self, parent, offset)
        (self.reason, self.time, self.drawable, self.port,) = unpack_from('xB2xIII', parent, offset)

class PortNotifyEvent(xcb.Event):
    def __init__(self, parent, offset=0):
        xcb.Event.__init__(self, parent, offset)
        (self.time, self.port, self.attribute, self.value,) = unpack_from('xx2xIIIi', parent, offset)

class QueryExtensionCookie(xcb.Cookie):
    pass

class QueryExtensionReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        (self.major, self.minor,) = unpack_from('xx2x4xHH', parent, offset)

class QueryAdaptorsCookie(xcb.Cookie):
    pass

class QueryAdaptorsReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        (self.num_adaptors,) = unpack_from('xx2x4xH22x', parent, offset)
        offset += 32
        self.info = xcb.List(parent, offset, self.num_adaptors, AdaptorInfo, -1)

class QueryEncodingsCookie(xcb.Cookie):
    pass

class QueryEncodingsReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        (self.num_encodings,) = unpack_from('xx2x4xH22x', parent, offset)
        offset += 32
        self.info = xcb.List(parent, offset, self.num_encodings, EncodingInfo, -1)

class GrabPortCookie(xcb.Cookie):
    pass

class GrabPortReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        (self.result,) = unpack_from('xB2x4x', parent, offset)

class QueryBestSizeCookie(xcb.Cookie):
    pass

class QueryBestSizeReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        (self.actual_width, self.actual_height,) = unpack_from('xx2x4xHH', parent, offset)

class GetPortAttributeCookie(xcb.Cookie):
    pass

class GetPortAttributeReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        (self.value,) = unpack_from('xx2x4xi', parent, offset)

class QueryPortAttributesCookie(xcb.Cookie):
    pass

class QueryPortAttributesReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        (self.num_attributes, self.text_size,) = unpack_from('xx2x4xII16x', parent, offset)
        offset += 32
        self.attributes = xcb.List(parent, offset, self.num_attributes, AttributeInfo, -1)

class ListImageFormatsCookie(xcb.Cookie):
    pass

class ListImageFormatsReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        (self.num_formats,) = unpack_from('xx2x4xI20x', parent, offset)
        offset += 32
        self.format = xcb.List(parent, offset, self.num_formats, ImageFormatInfo, 128)

class QueryImageAttributesCookie(xcb.Cookie):
    pass

class QueryImageAttributesReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        (self.num_planes, self.data_size, self.width, self.height,) = unpack_from('xx2x4xIIHH12x', parent, offset)
        offset += 32
        self.pitches = xcb.List(parent, offset, self.num_planes, 'I', 4)
        offset += len(self.pitches.buf())
        offset += xcb.type_pad(4, offset)
        self.offsets = xcb.List(parent, offset, self.num_planes, 'I', 4)

class xvExtension(xcb.Extension):

    def QueryExtension(self, ):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2x', ))
        return self.send_request(xcb.Request(buf.getvalue(), 0, False, True),
                                 QueryExtensionCookie(),
                                 QueryExtensionReply)

    def QueryExtensionUnchecked(self, ):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2x', ))
        return self.send_request(xcb.Request(buf.getvalue(), 0, False, False),
                                 QueryExtensionCookie(),
                                 QueryExtensionReply)

    def QueryAdaptors(self, window):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', window))
        return self.send_request(xcb.Request(buf.getvalue(), 1, False, True),
                                 QueryAdaptorsCookie(),
                                 QueryAdaptorsReply)

    def QueryAdaptorsUnchecked(self, window):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', window))
        return self.send_request(xcb.Request(buf.getvalue(), 1, False, False),
                                 QueryAdaptorsCookie(),
                                 QueryAdaptorsReply)

    def QueryEncodings(self, port):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', port))
        return self.send_request(xcb.Request(buf.getvalue(), 2, False, True),
                                 QueryEncodingsCookie(),
                                 QueryEncodingsReply)

    def QueryEncodingsUnchecked(self, port):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', port))
        return self.send_request(xcb.Request(buf.getvalue(), 2, False, False),
                                 QueryEncodingsCookie(),
                                 QueryEncodingsReply)

    def GrabPort(self, port, time):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xII', port, time))
        return self.send_request(xcb.Request(buf.getvalue(), 3, False, True),
                                 GrabPortCookie(),
                                 GrabPortReply)

    def GrabPortUnchecked(self, port, time):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xII', port, time))
        return self.send_request(xcb.Request(buf.getvalue(), 3, False, False),
                                 GrabPortCookie(),
                                 GrabPortReply)

    def UngrabPortChecked(self, port, time):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xII', port, time))
        return self.send_request(xcb.Request(buf.getvalue(), 4, True, True),
                                 xcb.VoidCookie())

    def UngrabPort(self, port, time):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xII', port, time))
        return self.send_request(xcb.Request(buf.getvalue(), 4, True, False),
                                 xcb.VoidCookie())

    def PutVideoChecked(self, port, drawable, gc, vid_x, vid_y, vid_w, vid_h, drw_x, drw_y, drw_w, drw_h):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIIIhhHHhhHH', port, drawable, gc, vid_x, vid_y, vid_w, vid_h, drw_x, drw_y, drw_w, drw_h))
        return self.send_request(xcb.Request(buf.getvalue(), 5, True, True),
                                 xcb.VoidCookie())

    def PutVideo(self, port, drawable, gc, vid_x, vid_y, vid_w, vid_h, drw_x, drw_y, drw_w, drw_h):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIIIhhHHhhHH', port, drawable, gc, vid_x, vid_y, vid_w, vid_h, drw_x, drw_y, drw_w, drw_h))
        return self.send_request(xcb.Request(buf.getvalue(), 5, True, False),
                                 xcb.VoidCookie())

    def PutStillChecked(self, port, drawable, gc, vid_x, vid_y, vid_w, vid_h, drw_x, drw_y, drw_w, drw_h):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIIIhhHHhhHH', port, drawable, gc, vid_x, vid_y, vid_w, vid_h, drw_x, drw_y, drw_w, drw_h))
        return self.send_request(xcb.Request(buf.getvalue(), 6, True, True),
                                 xcb.VoidCookie())

    def PutStill(self, port, drawable, gc, vid_x, vid_y, vid_w, vid_h, drw_x, drw_y, drw_w, drw_h):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIIIhhHHhhHH', port, drawable, gc, vid_x, vid_y, vid_w, vid_h, drw_x, drw_y, drw_w, drw_h))
        return self.send_request(xcb.Request(buf.getvalue(), 6, True, False),
                                 xcb.VoidCookie())

    def GetVideoChecked(self, port, drawable, gc, vid_x, vid_y, vid_w, vid_h, drw_x, drw_y, drw_w, drw_h):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIIIhhHHhhHH', port, drawable, gc, vid_x, vid_y, vid_w, vid_h, drw_x, drw_y, drw_w, drw_h))
        return self.send_request(xcb.Request(buf.getvalue(), 7, True, True),
                                 xcb.VoidCookie())

    def GetVideo(self, port, drawable, gc, vid_x, vid_y, vid_w, vid_h, drw_x, drw_y, drw_w, drw_h):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIIIhhHHhhHH', port, drawable, gc, vid_x, vid_y, vid_w, vid_h, drw_x, drw_y, drw_w, drw_h))
        return self.send_request(xcb.Request(buf.getvalue(), 7, True, False),
                                 xcb.VoidCookie())

    def GetStillChecked(self, port, drawable, gc, vid_x, vid_y, vid_w, vid_h, drw_x, drw_y, drw_w, drw_h):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIIIhhHHhhHH', port, drawable, gc, vid_x, vid_y, vid_w, vid_h, drw_x, drw_y, drw_w, drw_h))
        return self.send_request(xcb.Request(buf.getvalue(), 8, True, True),
                                 xcb.VoidCookie())

    def GetStill(self, port, drawable, gc, vid_x, vid_y, vid_w, vid_h, drw_x, drw_y, drw_w, drw_h):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIIIhhHHhhHH', port, drawable, gc, vid_x, vid_y, vid_w, vid_h, drw_x, drw_y, drw_w, drw_h))
        return self.send_request(xcb.Request(buf.getvalue(), 8, True, False),
                                 xcb.VoidCookie())

    def StopVideoChecked(self, port, drawable):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xII', port, drawable))
        return self.send_request(xcb.Request(buf.getvalue(), 9, True, True),
                                 xcb.VoidCookie())

    def StopVideo(self, port, drawable):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xII', port, drawable))
        return self.send_request(xcb.Request(buf.getvalue(), 9, True, False),
                                 xcb.VoidCookie())

    def SelectVideoNotifyChecked(self, drawable, onoff):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIB3x', drawable, onoff))
        return self.send_request(xcb.Request(buf.getvalue(), 10, True, True),
                                 xcb.VoidCookie())

    def SelectVideoNotify(self, drawable, onoff):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIB3x', drawable, onoff))
        return self.send_request(xcb.Request(buf.getvalue(), 10, True, False),
                                 xcb.VoidCookie())

    def SelectPortNotifyChecked(self, port, onoff):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIB3x', port, onoff))
        return self.send_request(xcb.Request(buf.getvalue(), 11, True, True),
                                 xcb.VoidCookie())

    def SelectPortNotify(self, port, onoff):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIB3x', port, onoff))
        return self.send_request(xcb.Request(buf.getvalue(), 11, True, False),
                                 xcb.VoidCookie())

    def QueryBestSize(self, port, vid_w, vid_h, drw_w, drw_h, motion):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIHHHHB3x', port, vid_w, vid_h, drw_w, drw_h, motion))
        return self.send_request(xcb.Request(buf.getvalue(), 12, False, True),
                                 QueryBestSizeCookie(),
                                 QueryBestSizeReply)

    def QueryBestSizeUnchecked(self, port, vid_w, vid_h, drw_w, drw_h, motion):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIHHHHB3x', port, vid_w, vid_h, drw_w, drw_h, motion))
        return self.send_request(xcb.Request(buf.getvalue(), 12, False, False),
                                 QueryBestSizeCookie(),
                                 QueryBestSizeReply)

    def SetPortAttributeChecked(self, port, attribute, value):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIIi', port, attribute, value))
        return self.send_request(xcb.Request(buf.getvalue(), 13, True, True),
                                 xcb.VoidCookie())

    def SetPortAttribute(self, port, attribute, value):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIIi', port, attribute, value))
        return self.send_request(xcb.Request(buf.getvalue(), 13, True, False),
                                 xcb.VoidCookie())

    def GetPortAttribute(self, port, attribute):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xII', port, attribute))
        return self.send_request(xcb.Request(buf.getvalue(), 14, False, True),
                                 GetPortAttributeCookie(),
                                 GetPortAttributeReply)

    def GetPortAttributeUnchecked(self, port, attribute):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xII', port, attribute))
        return self.send_request(xcb.Request(buf.getvalue(), 14, False, False),
                                 GetPortAttributeCookie(),
                                 GetPortAttributeReply)

    def QueryPortAttributes(self, port):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', port))
        return self.send_request(xcb.Request(buf.getvalue(), 15, False, True),
                                 QueryPortAttributesCookie(),
                                 QueryPortAttributesReply)

    def QueryPortAttributesUnchecked(self, port):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', port))
        return self.send_request(xcb.Request(buf.getvalue(), 15, False, False),
                                 QueryPortAttributesCookie(),
                                 QueryPortAttributesReply)

    def ListImageFormats(self, port):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', port))
        return self.send_request(xcb.Request(buf.getvalue(), 16, False, True),
                                 ListImageFormatsCookie(),
                                 ListImageFormatsReply)

    def ListImageFormatsUnchecked(self, port):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', port))
        return self.send_request(xcb.Request(buf.getvalue(), 16, False, False),
                                 ListImageFormatsCookie(),
                                 ListImageFormatsReply)

    def QueryImageAttributes(self, port, id, width, height):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIIHH', port, id, width, height))
        return self.send_request(xcb.Request(buf.getvalue(), 17, False, True),
                                 QueryImageAttributesCookie(),
                                 QueryImageAttributesReply)

    def QueryImageAttributesUnchecked(self, port, id, width, height):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIIHH', port, id, width, height))
        return self.send_request(xcb.Request(buf.getvalue(), 17, False, False),
                                 QueryImageAttributesCookie(),
                                 QueryImageAttributesReply)

    def PutImageChecked(self, port, drawable, gc, id, src_x, src_y, src_w, src_h, drw_x, drw_y, drw_w, drw_h, width, height, data_len, data):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIIIIhhHHhhHHHH', port, drawable, gc, id, src_x, src_y, src_w, src_h, drw_x, drw_y, drw_w, drw_h, width, height))
        buf.write(str(buffer(array('B', data))))
        return self.send_request(xcb.Request(buf.getvalue(), 18, True, True),
                                 xcb.VoidCookie())

    def PutImage(self, port, drawable, gc, id, src_x, src_y, src_w, src_h, drw_x, drw_y, drw_w, drw_h, width, height, data_len, data):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIIIIhhHHhhHHHH', port, drawable, gc, id, src_x, src_y, src_w, src_h, drw_x, drw_y, drw_w, drw_h, width, height))
        buf.write(str(buffer(array('B', data))))
        return self.send_request(xcb.Request(buf.getvalue(), 18, True, False),
                                 xcb.VoidCookie())

    def ShmPutImageChecked(self, port, drawable, gc, shmseg, id, offset, src_x, src_y, src_w, src_h, drw_x, drw_y, drw_w, drw_h, width, height, send_event):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIIIIIIhhHHhhHHHHB3x', port, drawable, gc, shmseg, id, offset, src_x, src_y, src_w, src_h, drw_x, drw_y, drw_w, drw_h, width, height, send_event))
        return self.send_request(xcb.Request(buf.getvalue(), 19, True, True),
                                 xcb.VoidCookie())

    def ShmPutImage(self, port, drawable, gc, shmseg, id, offset, src_x, src_y, src_w, src_h, drw_x, drw_y, drw_w, drw_h, width, height, send_event):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIIIIIIhhHHhhHHHHB3x', port, drawable, gc, shmseg, id, offset, src_x, src_y, src_w, src_h, drw_x, drw_y, drw_w, drw_h, width, height, send_event))
        return self.send_request(xcb.Request(buf.getvalue(), 19, True, False),
                                 xcb.VoidCookie())

_events = {
    0 : VideoNotifyEvent,
    1 : PortNotifyEvent,
}

_errors = {
    0 : (PortError, BadPort),
    1 : (EncodingError, BadEncoding),
    2 : (ControlError, BadControl),
}

xcb._add_ext(key, xvExtension, _events, _errors)
