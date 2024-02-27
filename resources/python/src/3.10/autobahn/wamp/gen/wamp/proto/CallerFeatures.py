# automatically generated by the FlatBuffers compiler, do not modify

# namespace: proto

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class CallerFeatures(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = CallerFeatures()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsCallerFeatures(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # CallerFeatures
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # CallerFeatures
    def CallerIdentification(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # CallerFeatures
    def CallTimeout(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # CallerFeatures
    def CallCanceling(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # CallerFeatures
    def ProgressiveCallResults(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # CallerFeatures
    def PayloadTransparency(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # CallerFeatures
    def PayloadEncryptionCryptobox(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

def CallerFeaturesStart(builder): builder.StartObject(6)
def Start(builder):
    return CallerFeaturesStart(builder)
def CallerFeaturesAddCallerIdentification(builder, callerIdentification): builder.PrependBoolSlot(0, callerIdentification, 0)
def AddCallerIdentification(builder, callerIdentification):
    return CallerFeaturesAddCallerIdentification(builder, callerIdentification)
def CallerFeaturesAddCallTimeout(builder, callTimeout): builder.PrependBoolSlot(1, callTimeout, 0)
def AddCallTimeout(builder, callTimeout):
    return CallerFeaturesAddCallTimeout(builder, callTimeout)
def CallerFeaturesAddCallCanceling(builder, callCanceling): builder.PrependBoolSlot(2, callCanceling, 0)
def AddCallCanceling(builder, callCanceling):
    return CallerFeaturesAddCallCanceling(builder, callCanceling)
def CallerFeaturesAddProgressiveCallResults(builder, progressiveCallResults): builder.PrependBoolSlot(3, progressiveCallResults, 0)
def AddProgressiveCallResults(builder, progressiveCallResults):
    return CallerFeaturesAddProgressiveCallResults(builder, progressiveCallResults)
def CallerFeaturesAddPayloadTransparency(builder, payloadTransparency): builder.PrependBoolSlot(4, payloadTransparency, 0)
def AddPayloadTransparency(builder, payloadTransparency):
    return CallerFeaturesAddPayloadTransparency(builder, payloadTransparency)
def CallerFeaturesAddPayloadEncryptionCryptobox(builder, payloadEncryptionCryptobox): builder.PrependBoolSlot(5, payloadEncryptionCryptobox, 0)
def AddPayloadEncryptionCryptobox(builder, payloadEncryptionCryptobox):
    return CallerFeaturesAddPayloadEncryptionCryptobox(builder, payloadEncryptionCryptobox)
def CallerFeaturesEnd(builder): return builder.EndObject()
def End(builder):
    return CallerFeaturesEnd(builder)