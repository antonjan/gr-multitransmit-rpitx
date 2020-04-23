#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Multitransmit for RpiTX
# Generated: Thu Apr 23 09:46:31 2020
##################################################

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt5 import Qt
from PyQt5 import Qt, QtCore
from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from grc_gnuradio import blks2 as grc_blks2
from optparse import OptionParser
import sip
import sys
from gnuradio import qtgui


class gr_multitransmit_rpitx(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Multitransmit for RpiTX")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Multitransmit for RpiTX")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "gr_multitransmit_rpitx")
        self.restoreGeometry(self.settings.value("geometry", type=QtCore.QByteArray))


        ##################################################
        # Variables
        ##################################################
        self.wfm_on = wfm_on = False
        self.usb_on = usb_on = False
        self.test_tone_frequency = test_tone_frequency = 1000
        self.rpitx_frequency_correction = rpitx_frequency_correction = 0
        self.ptt_lock = ptt_lock = False
        self.ptt = ptt = False
        self.nfm_on = nfm_on = False
        self.lsb_on = lsb_on = False
        self.low_frequency_cutoff = low_frequency_cutoff = 200
        self.high_frequency_cutoff = high_frequency_cutoff = 2500
        self.enable_tone = enable_tone = False
        self.enable_test_tone = enable_test_tone = False
        self.ctcss_tone = ctcss_tone = 100
        self.audio_rate = audio_rate = 48000
        self.am_on = am_on = False

        ##################################################
        # Blocks
        ##################################################
        _wfm_on_check_box = Qt.QCheckBox('WFM')
        self._wfm_on_choices = {True: True, False: False}
        self._wfm_on_choices_inv = dict((v,k) for k,v in self._wfm_on_choices.iteritems())
        self._wfm_on_callback = lambda i: Qt.QMetaObject.invokeMethod(_wfm_on_check_box, "setChecked", Qt.Q_ARG("bool", self._wfm_on_choices_inv[i]))
        self._wfm_on_callback(self.wfm_on)
        _wfm_on_check_box.stateChanged.connect(lambda i: self.set_wfm_on(self._wfm_on_choices[bool(i)]))
        self.top_grid_layout.addWidget(_wfm_on_check_box, 4, 0, 1, 1)
        for r in range(4, 5):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        _usb_on_check_box = Qt.QCheckBox('USB')
        self._usb_on_choices = {True: True, False: False}
        self._usb_on_choices_inv = dict((v,k) for k,v in self._usb_on_choices.iteritems())
        self._usb_on_callback = lambda i: Qt.QMetaObject.invokeMethod(_usb_on_check_box, "setChecked", Qt.Q_ARG("bool", self._usb_on_choices_inv[i]))
        self._usb_on_callback(self.usb_on)
        _usb_on_check_box.stateChanged.connect(lambda i: self.set_usb_on(self._usb_on_choices[bool(i)]))
        self.top_grid_layout.addWidget(_usb_on_check_box, 5, 0, 1, 1)
        for r in range(5, 6):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._test_tone_frequency_range = Range(0, audio_rate, 1, 1000, 200)
        self._test_tone_frequency_win = RangeWidget(self._test_tone_frequency_range, self.set_test_tone_frequency, 'Tone Frequency', "counter", float)
        self.top_grid_layout.addWidget(self._test_tone_frequency_win, 11, 1, 1, 1)
        for r in range(11, 12):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._rpitx_frequency_correction_range = Range(-24, 24, .1, 0, 200)
        self._rpitx_frequency_correction_win = RangeWidget(self._rpitx_frequency_correction_range, self.set_rpitx_frequency_correction, 'RpiTX Frequency Correction', "counter_slider", float)
        self.top_grid_layout.addWidget(self._rpitx_frequency_correction_win, 13, 0, 1, 1)
        for r in range(13, 14):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        _ptt_lock_check_box = Qt.QCheckBox('PTT Lock')
        self._ptt_lock_choices = {True: True, False: False}
        self._ptt_lock_choices_inv = dict((v,k) for k,v in self._ptt_lock_choices.iteritems())
        self._ptt_lock_callback = lambda i: Qt.QMetaObject.invokeMethod(_ptt_lock_check_box, "setChecked", Qt.Q_ARG("bool", self._ptt_lock_choices_inv[i]))
        self._ptt_lock_callback(self.ptt_lock)
        _ptt_lock_check_box.stateChanged.connect(lambda i: self.set_ptt_lock(self._ptt_lock_choices[bool(i)]))
        self.top_grid_layout.addWidget(_ptt_lock_check_box, 0, 1, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        _ptt_push_button = Qt.QPushButton('Push To Talk')
        self._ptt_choices = {'Pressed': True, 'Released': False}
        _ptt_push_button.pressed.connect(lambda: self.set_ptt(self._ptt_choices['Pressed']))
        _ptt_push_button.released.connect(lambda: self.set_ptt(self._ptt_choices['Released']))
        self.top_grid_layout.addWidget(_ptt_push_button, 0, 0, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        _nfm_on_check_box = Qt.QCheckBox('NFM')
        self._nfm_on_choices = {True: True, False: False}
        self._nfm_on_choices_inv = dict((v,k) for k,v in self._nfm_on_choices.iteritems())
        self._nfm_on_callback = lambda i: Qt.QMetaObject.invokeMethod(_nfm_on_check_box, "setChecked", Qt.Q_ARG("bool", self._nfm_on_choices_inv[i]))
        self._nfm_on_callback(self.nfm_on)
        _nfm_on_check_box.stateChanged.connect(lambda i: self.set_nfm_on(self._nfm_on_choices[bool(i)]))
        self.top_grid_layout.addWidget(_nfm_on_check_box, 3, 0, 1, 1)
        for r in range(3, 4):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        _lsb_on_check_box = Qt.QCheckBox('LSB')
        self._lsb_on_choices = {True: True, False: False}
        self._lsb_on_choices_inv = dict((v,k) for k,v in self._lsb_on_choices.iteritems())
        self._lsb_on_callback = lambda i: Qt.QMetaObject.invokeMethod(_lsb_on_check_box, "setChecked", Qt.Q_ARG("bool", self._lsb_on_choices_inv[i]))
        self._lsb_on_callback(self.lsb_on)
        _lsb_on_check_box.stateChanged.connect(lambda i: self.set_lsb_on(self._lsb_on_choices[bool(i)]))
        self.top_grid_layout.addWidget(_lsb_on_check_box, 6, 0, 1, 1)
        for r in range(6, 7):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._low_frequency_cutoff_range = Range(1, audio_rate/2, 1, 200, 100)
        self._low_frequency_cutoff_win = RangeWidget(self._low_frequency_cutoff_range, self.set_low_frequency_cutoff, 'Low Frequency Cutoff', "counter_slider", float)
        self.top_grid_layout.addWidget(self._low_frequency_cutoff_win, 7, 0, 1, 1)
        for r in range(7, 8):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._high_frequency_cutoff_range = Range(1, audio_rate/2, 1, 2500, 100)
        self._high_frequency_cutoff_win = RangeWidget(self._high_frequency_cutoff_range, self.set_high_frequency_cutoff, 'High Frequency Cutoff', "counter_slider", float)
        self.top_grid_layout.addWidget(self._high_frequency_cutoff_win, 7, 1, 1, 1)
        for r in range(7, 8):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        _enable_tone_check_box = Qt.QCheckBox('CTCSS Tone Enable')
        self._enable_tone_choices = {True: True, False: False}
        self._enable_tone_choices_inv = dict((v,k) for k,v in self._enable_tone_choices.iteritems())
        self._enable_tone_callback = lambda i: Qt.QMetaObject.invokeMethod(_enable_tone_check_box, "setChecked", Qt.Q_ARG("bool", self._enable_tone_choices_inv[i]))
        self._enable_tone_callback(self.enable_tone)
        _enable_tone_check_box.stateChanged.connect(lambda i: self.set_enable_tone(self._enable_tone_choices[bool(i)]))
        self.top_grid_layout.addWidget(_enable_tone_check_box, 10, 0, 1, 1)
        for r in range(10, 11):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        _enable_test_tone_check_box = Qt.QCheckBox('Test Tone')
        self._enable_test_tone_choices = {True: True, False: False}
        self._enable_test_tone_choices_inv = dict((v,k) for k,v in self._enable_test_tone_choices.iteritems())
        self._enable_test_tone_callback = lambda i: Qt.QMetaObject.invokeMethod(_enable_test_tone_check_box, "setChecked", Qt.Q_ARG("bool", self._enable_test_tone_choices_inv[i]))
        self._enable_test_tone_callback(self.enable_test_tone)
        _enable_test_tone_check_box.stateChanged.connect(lambda i: self.set_enable_test_tone(self._enable_test_tone_choices[bool(i)]))
        self.top_grid_layout.addWidget(_enable_test_tone_check_box, 11, 0, 1, 1)
        for r in range(11, 12):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._ctcss_tone_range = Range(67, 254.1, .1, 100, 200)
        self._ctcss_tone_win = RangeWidget(self._ctcss_tone_range, self.set_ctcss_tone, 'CTCSS Tone', "counter", float)
        self.top_grid_layout.addWidget(self._ctcss_tone_win, 10, 1, 1, 1)
        for r in range(10, 11):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        _am_on_check_box = Qt.QCheckBox('AM')
        self._am_on_choices = {True: True, False: False}
        self._am_on_choices_inv = dict((v,k) for k,v in self._am_on_choices.iteritems())
        self._am_on_callback = lambda i: Qt.QMetaObject.invokeMethod(_am_on_check_box, "setChecked", Qt.Q_ARG("bool", self._am_on_choices_inv[i]))
        self._am_on_callback(self.am_on)
        _am_on_check_box.stateChanged.connect(lambda i: self.set_am_on(self._am_on_choices[bool(i)]))
        self.top_grid_layout.addWidget(_am_on_check_box, 2, 0, 1, 1)
        for r in range(2, 3):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.rational_resampler_wfm = filter.rational_resampler_ccc(
                interpolation=audio_rate,
                decimation=audio_rate*4,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_nbfm = filter.rational_resampler_ccc(
                interpolation=audio_rate,
                decimation=audio_rate*2,
                taps=None,
                fractional_bw=None,
        )
        self.qtgui_waterfall_sink_rpitx = qtgui.waterfall_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	audio_rate, #bw
        	"rpitx signal (I/Q)", #name
                1 #number of inputs
        )
        self.qtgui_waterfall_sink_rpitx.set_update_time(0.01)
        self.qtgui_waterfall_sink_rpitx.enable_grid(False)
        self.qtgui_waterfall_sink_rpitx.enable_axis_labels(True)

        if not True:
          self.qtgui_waterfall_sink_rpitx.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_waterfall_sink_rpitx.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_rpitx.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_rpitx.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_rpitx.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_rpitx.set_line_alpha(i, alphas[i])

        self.qtgui_waterfall_sink_rpitx.set_intensity_range(-140, 10)

        self._qtgui_waterfall_sink_rpitx_win = sip.wrapinstance(self.qtgui_waterfall_sink_rpitx.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_waterfall_sink_rpitx_win, 1, 1, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_sink_transmit = qtgui.sink_c(
        	1024, #fftsize
        	firdes.WIN_HAMMING, #wintype
        	0, #fc
        	audio_rate, #bw
        	"Transmitted Signal (I/Q)", #name
        	True, #plotfreq
        	True, #plotwaterfall
        	True, #plottime
        	True, #plotconst
        )
        self.qtgui_sink_transmit.set_update_time(1.0/100)
        self._qtgui_sink_transmit_win = sip.wrapinstance(self.qtgui_sink_transmit.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_sink_transmit_win, 1, 0, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)


        self.qtgui_sink_transmit.enable_rf_freq(False)



        self.low_pass_filter_nbfm = filter.fir_filter_fff(1, firdes.low_pass(
        	1, audio_rate, 4e3, 500, firdes.WIN_HAMMING, 6.76))
        self.freq_xlating_fir_filter_rpitx = filter.freq_xlating_fir_filter_ccc(1, ([1]), -rpitx_frequency_correction*1000, 48000)
        self.blocks_multiply_usb = blocks.multiply_vcc(1)
        self.blocks_multiply_lsb = blocks.multiply_vcc(1)
        self.blocks_multiply_const_wfm = blocks.multiply_const_vcc((wfm_on, ))
        self.blocks_multiply_const_test = blocks.multiply_const_vff((enable_test_tone, ))
        self.blocks_multiply_const_rpitx = blocks.multiply_const_vcc((ptt or ptt_lock, ))
        self.blocks_multiply_const_nbfm = blocks.multiply_const_vcc((nfm_on, ))
        self.blocks_multiply_const_ctcss = blocks.multiply_const_vff((enable_tone, ))
        self.blocks_multiply_am = blocks.multiply_vcc(1)
        self.blocks_float_to_complex_am_ssb = blocks.float_to_complex(1)
        self.blocks_add_nbfm = blocks.add_vff(1)
        self.blocks_add_fm = blocks.add_vcc(1)
        self.blocks_add_const_am = blocks.add_const_vcc((.5, ))
        self.blocks_add_am_ssb_fm = blocks.add_vcc(1)
        self.blocks_add_am_ssb = blocks.add_vcc(1)
        self.blocks_add = blocks.add_vff(1)
        self.blks_tcp_sink_rpitx = grc_blks2.tcp_sink(
        	itemsize=gr.sizeof_gr_complex*1,
        	addr='192.168.0.x',
        	port=8011,
        	server=False,
        )
        self.band_pass_filter_usb = filter.interp_fir_filter_ccc(1, firdes.complex_band_pass(
        	1, audio_rate, low_frequency_cutoff, high_frequency_cutoff, 200, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_lsb = filter.interp_fir_filter_ccc(1, firdes.complex_band_pass(
        	1, audio_rate, -high_frequency_cutoff, -low_frequency_cutoff, 200, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_am = filter.fir_filter_ccf(1, firdes.band_pass(
        	1, audio_rate, low_frequency_cutoff, high_frequency_cutoff, 400, firdes.WIN_HAMMING, 6.76))
        self.audio_source = audio.source(48000, '', True)
        self.analog_wfm_tx = analog.wfm_tx(
        	audio_rate=audio_rate,
        	quad_rate=audio_rate * 4,
        	tau=75e-6,
        	max_dev=75e3,
        	fh=-1.0,
        )
        self.analog_sig_source_usb = analog.sig_source_c(audio_rate, analog.GR_COS_WAVE, 0, 1.8 if usb_on else 0, 0)
        self.analog_sig_source_test = analog.sig_source_f(audio_rate, analog.GR_SIN_WAVE, test_tone_frequency, .3, 0)
        self.analog_sig_source_lsb = analog.sig_source_c(audio_rate, analog.GR_COS_WAVE, 0, 1.8 if lsb_on else 0, 0)
        self.analog_sig_source_ctcss = analog.sig_source_f(audio_rate, analog.GR_COS_WAVE, ctcss_tone, 0.1, 0)
        self.analog_sig_source_am = analog.sig_source_c(audio_rate, analog.GR_COS_WAVE, 0, 1 if am_on else 0, 0)
        self.analog_nbfm_tx = analog.nbfm_tx(
        	audio_rate=audio_rate,
        	quad_rate=audio_rate*2,
        	tau=75e-6,
        	max_dev=5e3,
        	fh=-1.0,
                )
        self.analog_const_source = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, 0)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_const_source, 0), (self.blocks_float_to_complex_am_ssb, 1))
        self.connect((self.analog_nbfm_tx, 0), (self.blocks_multiply_const_nbfm, 0))
        self.connect((self.analog_sig_source_am, 0), (self.blocks_multiply_am, 1))
        self.connect((self.analog_sig_source_ctcss, 0), (self.blocks_multiply_const_ctcss, 0))
        self.connect((self.analog_sig_source_lsb, 0), (self.blocks_multiply_lsb, 1))
        self.connect((self.analog_sig_source_test, 0), (self.blocks_multiply_const_test, 0))
        self.connect((self.analog_sig_source_usb, 0), (self.blocks_multiply_usb, 1))
        self.connect((self.analog_wfm_tx, 0), (self.blocks_multiply_const_wfm, 0))
        self.connect((self.audio_source, 0), (self.blocks_add, 0))
        self.connect((self.band_pass_filter_am, 0), (self.blocks_add_const_am, 0))
        self.connect((self.band_pass_filter_lsb, 0), (self.blocks_multiply_lsb, 0))
        self.connect((self.band_pass_filter_usb, 0), (self.blocks_multiply_usb, 0))
        self.connect((self.blocks_add, 0), (self.analog_wfm_tx, 0))
        self.connect((self.blocks_add, 0), (self.blocks_add_nbfm, 1))
        self.connect((self.blocks_add, 0), (self.blocks_float_to_complex_am_ssb, 0))
        self.connect((self.blocks_add_am_ssb, 0), (self.blocks_add_am_ssb_fm, 1))
        self.connect((self.blocks_add_am_ssb_fm, 0), (self.blocks_multiply_const_rpitx, 0))
        self.connect((self.blocks_add_const_am, 0), (self.blocks_multiply_am, 0))
        self.connect((self.blocks_add_fm, 0), (self.blocks_add_am_ssb_fm, 0))
        self.connect((self.blocks_add_nbfm, 0), (self.low_pass_filter_nbfm, 0))
        self.connect((self.blocks_float_to_complex_am_ssb, 0), (self.band_pass_filter_am, 0))
        self.connect((self.blocks_float_to_complex_am_ssb, 0), (self.band_pass_filter_lsb, 0))
        self.connect((self.blocks_float_to_complex_am_ssb, 0), (self.band_pass_filter_usb, 0))
        self.connect((self.blocks_multiply_am, 0), (self.blocks_add_am_ssb, 0))
        self.connect((self.blocks_multiply_const_ctcss, 0), (self.blocks_add_nbfm, 0))
        self.connect((self.blocks_multiply_const_nbfm, 0), (self.rational_resampler_nbfm, 0))
        self.connect((self.blocks_multiply_const_rpitx, 0), (self.freq_xlating_fir_filter_rpitx, 0))
        self.connect((self.blocks_multiply_const_rpitx, 0), (self.qtgui_sink_transmit, 0))
        self.connect((self.blocks_multiply_const_test, 0), (self.blocks_add, 1))
        self.connect((self.blocks_multiply_const_wfm, 0), (self.rational_resampler_wfm, 0))
        self.connect((self.blocks_multiply_lsb, 0), (self.blocks_add_am_ssb, 1))
        self.connect((self.blocks_multiply_usb, 0), (self.blocks_add_am_ssb, 2))
        self.connect((self.freq_xlating_fir_filter_rpitx, 0), (self.blks_tcp_sink_rpitx, 0))
        self.connect((self.freq_xlating_fir_filter_rpitx, 0), (self.qtgui_waterfall_sink_rpitx, 0))
        self.connect((self.low_pass_filter_nbfm, 0), (self.analog_nbfm_tx, 0))
        self.connect((self.rational_resampler_nbfm, 0), (self.blocks_add_fm, 0))
        self.connect((self.rational_resampler_wfm, 0), (self.blocks_add_fm, 1))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "gr_multitransmit_rpitx")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_wfm_on(self):
        return self.wfm_on

    def set_wfm_on(self, wfm_on):
        self.wfm_on = wfm_on
        self._wfm_on_callback(self.wfm_on)
        self.blocks_multiply_const_wfm.set_k((self.wfm_on, ))

    def get_usb_on(self):
        return self.usb_on

    def set_usb_on(self, usb_on):
        self.usb_on = usb_on
        self._usb_on_callback(self.usb_on)
        self.analog_sig_source_usb.set_amplitude(1.8 if self.usb_on else 0)

    def get_test_tone_frequency(self):
        return self.test_tone_frequency

    def set_test_tone_frequency(self, test_tone_frequency):
        self.test_tone_frequency = test_tone_frequency
        self.analog_sig_source_test.set_frequency(self.test_tone_frequency)

    def get_rpitx_frequency_correction(self):
        return self.rpitx_frequency_correction

    def set_rpitx_frequency_correction(self, rpitx_frequency_correction):
        self.rpitx_frequency_correction = rpitx_frequency_correction
        self.freq_xlating_fir_filter_rpitx.set_center_freq(-self.rpitx_frequency_correction*1000)

    def get_ptt_lock(self):
        return self.ptt_lock

    def set_ptt_lock(self, ptt_lock):
        self.ptt_lock = ptt_lock
        self._ptt_lock_callback(self.ptt_lock)
        self.blocks_multiply_const_rpitx.set_k((self.ptt or self.ptt_lock, ))

    def get_ptt(self):
        return self.ptt

    def set_ptt(self, ptt):
        self.ptt = ptt
        self.blocks_multiply_const_rpitx.set_k((self.ptt or self.ptt_lock, ))

    def get_nfm_on(self):
        return self.nfm_on

    def set_nfm_on(self, nfm_on):
        self.nfm_on = nfm_on
        self._nfm_on_callback(self.nfm_on)
        self.blocks_multiply_const_nbfm.set_k((self.nfm_on, ))

    def get_lsb_on(self):
        return self.lsb_on

    def set_lsb_on(self, lsb_on):
        self.lsb_on = lsb_on
        self._lsb_on_callback(self.lsb_on)
        self.analog_sig_source_lsb.set_amplitude(1.8 if self.lsb_on else 0)

    def get_low_frequency_cutoff(self):
        return self.low_frequency_cutoff

    def set_low_frequency_cutoff(self, low_frequency_cutoff):
        self.low_frequency_cutoff = low_frequency_cutoff
        self.band_pass_filter_usb.set_taps(firdes.complex_band_pass(1, self.audio_rate, self.low_frequency_cutoff, self.high_frequency_cutoff, 200, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_lsb.set_taps(firdes.complex_band_pass(1, self.audio_rate, -self.high_frequency_cutoff, -self.low_frequency_cutoff, 200, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_am.set_taps(firdes.band_pass(1, self.audio_rate, self.low_frequency_cutoff, self.high_frequency_cutoff, 400, firdes.WIN_HAMMING, 6.76))

    def get_high_frequency_cutoff(self):
        return self.high_frequency_cutoff

    def set_high_frequency_cutoff(self, high_frequency_cutoff):
        self.high_frequency_cutoff = high_frequency_cutoff
        self.band_pass_filter_usb.set_taps(firdes.complex_band_pass(1, self.audio_rate, self.low_frequency_cutoff, self.high_frequency_cutoff, 200, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_lsb.set_taps(firdes.complex_band_pass(1, self.audio_rate, -self.high_frequency_cutoff, -self.low_frequency_cutoff, 200, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_am.set_taps(firdes.band_pass(1, self.audio_rate, self.low_frequency_cutoff, self.high_frequency_cutoff, 400, firdes.WIN_HAMMING, 6.76))

    def get_enable_tone(self):
        return self.enable_tone

    def set_enable_tone(self, enable_tone):
        self.enable_tone = enable_tone
        self._enable_tone_callback(self.enable_tone)
        self.blocks_multiply_const_ctcss.set_k((self.enable_tone, ))

    def get_enable_test_tone(self):
        return self.enable_test_tone

    def set_enable_test_tone(self, enable_test_tone):
        self.enable_test_tone = enable_test_tone
        self._enable_test_tone_callback(self.enable_test_tone)
        self.blocks_multiply_const_test.set_k((self.enable_test_tone, ))

    def get_ctcss_tone(self):
        return self.ctcss_tone

    def set_ctcss_tone(self, ctcss_tone):
        self.ctcss_tone = ctcss_tone
        self.analog_sig_source_ctcss.set_frequency(self.ctcss_tone)

    def get_audio_rate(self):
        return self.audio_rate

    def set_audio_rate(self, audio_rate):
        self.audio_rate = audio_rate
        self.qtgui_waterfall_sink_rpitx.set_frequency_range(0, self.audio_rate)
        self.qtgui_sink_transmit.set_frequency_range(0, self.audio_rate)
        self.low_pass_filter_nbfm.set_taps(firdes.low_pass(1, self.audio_rate, 4e3, 500, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_usb.set_taps(firdes.complex_band_pass(1, self.audio_rate, self.low_frequency_cutoff, self.high_frequency_cutoff, 200, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_lsb.set_taps(firdes.complex_band_pass(1, self.audio_rate, -self.high_frequency_cutoff, -self.low_frequency_cutoff, 200, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_am.set_taps(firdes.band_pass(1, self.audio_rate, self.low_frequency_cutoff, self.high_frequency_cutoff, 400, firdes.WIN_HAMMING, 6.76))
        self.analog_sig_source_usb.set_sampling_freq(self.audio_rate)
        self.analog_sig_source_test.set_sampling_freq(self.audio_rate)
        self.analog_sig_source_lsb.set_sampling_freq(self.audio_rate)
        self.analog_sig_source_ctcss.set_sampling_freq(self.audio_rate)
        self.analog_sig_source_am.set_sampling_freq(self.audio_rate)

    def get_am_on(self):
        return self.am_on

    def set_am_on(self, am_on):
        self.am_on = am_on
        self._am_on_callback(self.am_on)
        self.analog_sig_source_am.set_amplitude(1 if self.am_on else 0)


def main(top_block_cls=gr_multitransmit_rpitx, options=None):

    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
