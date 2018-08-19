#
# This file generated automatically from shm.xml by py_client.py.
# Edit at your peril.
#

import xcb
import cStringIO
from struct import pack, unpack_from
from array import array
import xproto

MAJOR_VERSION = 1
MINOR_VERSION = 2

key = xcb.ExtensionKey('MIT-SHM')

class CompletionEvent(xcb.Event):
    def __init__(self, parent, offset=0):
        xcb.Event.__init__(self, parent, offset)
        (self.drawable, self.minor_event, self.major_event, self.shmseg, self.offset,) = unpack_from('xx2xIHBxII', parent, offset)

class SegError(xcb.Error):
    def __init__(self, parent, offset=0):
        xcb.Error.__init__(self, parent, offset)
        (self.bad_value, self.minor_opcode, self.major_opcode,) = unpack_from('xx2xIHBx', parent, offset)

class BadSeg(xcb.ProtocolException):
    pass

class QueryVersionCookie(xcb.Cookie):
    pass

class QueryVersionReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        (self.shared_pixmaps, self.major_version, self.minor_version, self.uid, self.gid, self.pixmap_format,) = unpack_from('xB2x4xHHHHB15x', parent, offset)

class GetImageCookie(xcb.Cookie):
    pass

class GetImageReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        (self.depth, self.visual, self.size,) = unpack_from('xB2x4xII', parent, offset)

class CreateSegmentCookie(xcb.Cookie):
    pass

class CreateSegmentReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        (self.nfd, self.shm_fd,) = unpack_from('xB2x4xi24x', parent, offset)

class shmExtension(xcb.Extension):

    def QueryVersion(self, ):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2x', ))
        return self.send_request(xcb.Request(buf.getvalue(), 0, False, True),
                                 QueryVersionCookie(),
                                 QueryVersionReply)

    def QueryVersionUnchecked(self, ):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2x', ))
        return self.send_request(xcb.Request(buf.getvalue(), 0, False, False),
                                 QueryVersionCookie(),
                                 QueryVersionReply)

    def AttachChecked(self, shmseg, shmid, read_only):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIIB3x', shmseg, shmid, read_only))
        return self.send_request(xcb.Request(buf.getvalue(), 1, True, True),
                                 xcb.VoidCookie())

    def Attach(self, shmseg, shmid, read_only):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIIB3x', shmseg, shmid, read_only))
        return self.send_request(xcb.Request(buf.getvalue(), 1, True, False),
                                 xcb.VoidCookie())

    def DetachChecked(self, shmseg):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', shmseg))
        return self.send_request(xcb.Request(buf.getvalue(), 2, True, True),
                                 xcb.VoidCookie())

    def Detach(self, shmseg):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', shmseg))
        return self.send_request(xcb.Request(buf.getvalue(), 2, True, False),
                                 xcb.VoidCookie())

    def PutImageChecked(self, drawable, gc, total_width, total_height, src_x, src_y, src_width, src_height, dst_x, dst_y, depth, format, send_event, shmseg, offset):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIIHHHHHHhhBBBxII', drawable, gc, total_width, total_height, src_x, src_y, src_width, src_height, dst_x, dst_y, depth, format, send_event, shmseg, offset))
        return self.send_request(xcb.Request(buf.getvalue(), 3, True, True),
                                 xcb.VoidCookie())

    def PutImage(self, drawable, gc, total_width, total_height, src_x, src_y, src_width, src_height, dst_x, dst_y, depth, format, send_event, shmseg, offset):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIIHHHHHHhhBBBxII', drawable, gc, total_width, total_height, src_x, src_y, src_width, src_height, dst_x, dst_y, depth, format, send_event, shmseg, offset))
        return self.send_request(xcb.Request(buf.getvalue(), 3, True, False),
                                 xcb.VoidCookie())

    def GetImage(self, drawable, x, y, width, height, plane_mask, format, shmseg, offset):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIhhHHIB3xII', drawable, x, y, width, height, plane_mask, format, shmseg, offset))
        return self.send_request(xcb.Request(buf.getvalue(), 4, False, True),
                                 GetImageCookie(),
                                 GetImageReply)

    def GetImageUnchecked(self, drawable, x, y, width, height, plane_mask, format, shmseg, offset):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIhhHHIB3xII', drawable, x, y, width, height, plane_mask, format, shmseg, offset))
        return self.send_request(xcb.Request(buf.getvalue(), 4, False, False),
                                 GetImageCookie(),
                                 GetImageReply)

    def CreatePixmapChecked(self, pid, drawable, width, height, depth, shmseg, offset):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIIHHB3xII', pid, drawable, width, height, depth, shmseg, offset))
        return self.send_request(xcb.Request(buf.getvalue(), 5, True, True),
                                 xcb.VoidCookie())

    def CreatePixmap(self, pid, drawable, width, height, depth, shmseg, offset):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIIHHB3xII', pid, drawable, width, height, depth, shmseg, offset))
        return self.send_request(xcb.Request(buf.getvalue(), 5, True, False),
                                 xcb.VoidCookie())

    def AttachFdChecked(self, shmseg, shm_fd, read_only):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIB3x', shmseg, read_only))
        return self.send_request(xcb.Request(buf.getvalue(), 6, True, True),
                                 xcb.VoidCookie())

    def AttachFd(self, shmseg, shm_fd, read_only):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIB3x', shmseg, read_only))
        return self.send_request(xcb.Request(buf.getvalue(), 6, True, False),
                                 xcb.VoidCookie())

    def CreateSegment(self, shmseg, size, read_only):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIIB3x', shmseg, size, read_only))
        return self.send_request(xcb.Request(buf.getvalue(), 7, False, True),
                                 CreateSegmentCookie(),
                                 CreateSegmentReply)

    def CreateSegmentUnchecked(self, shmseg, size, read_only):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIIB3x', shmseg, size, read_only))
        return self.send_request(xcb.Request(buf.getvalue(), 7, False, False),
                                 CreateSegmentCookie(),
                                 CreateSegmentReply)

_events = {
    0 : CompletionEvent,
}

_errors = {
    0 : (SegError, BadSeg),
}

xcb._add_ext(key, shmExtension, _events, _errors)
