#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Sat Jan 12 15:07:28 2019
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

import os
import sys
sys.path.append(os.environ.get('GRC_HIER_PATH', os.path.expanduser('~/.grc_gnuradio')))

from PyQt4 import Qt
from SekizKanalFFT import SekizKanalFFT  # grc-generated hier_block
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import sip


class top_block(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Top Block")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Top Block")
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

        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 32000

        ##################################################
        # Blocks
        ##################################################
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
        	96, #size
        	samp_rate, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(20, 150)
        
        self.qtgui_time_sink_x_0.set_y_label("Amplitude", "")
        
        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(True)
        self.qtgui_time_sink_x_0.enable_grid(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_time_sink_x_0.disable_legend()
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_win)
        self.blocks_null_sink_3 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.blocks_null_sink_2 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.blocks_null_sink_1 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.blocks_null_sink_0_0_1 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.blocks_null_sink_0_0_0 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.blocks_multiply_conjugate_cc_0 = blocks.multiply_conjugate_cc(1)
        self.blocks_keep_m_in_n_0_0 = blocks.keep_m_in_n(gr.sizeof_gr_complex, 1, 96, 38)
        self.blocks_keep_m_in_n_0 = blocks.keep_m_in_n(gr.sizeof_gr_complex, 1, 96, 38)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_int*1, "/home/nvidia/gitDir/gr-work/fft_yon_sim_10Mcenter_30degree.bin", False)
        self.blocks_file_sink_3 = blocks.file_sink(gr.sizeof_gr_complex*1, "fft0.bin", False)
        self.blocks_file_sink_3.set_unbuffered(False)
        self.blocks_file_sink_2_0 = blocks.file_sink(gr.sizeof_gr_complex*1, "fazfarki.bin", False)
        self.blocks_file_sink_2_0.set_unbuffered(False)
        self.blocks_file_sink_2 = blocks.file_sink(gr.sizeof_float*1, "genlik0.bin", False)
        self.blocks_file_sink_2.set_unbuffered(False)
        self.blocks_file_sink_1 = blocks.file_sink(gr.sizeof_float*1, "faz0.bin", False)
        self.blocks_file_sink_1.set_unbuffered(False)
        self.blocks_complex_to_mag_0_0 = blocks.complex_to_mag(1)
        self.blocks_complex_to_mag_0 = blocks.complex_to_mag(1)
        self.blocks_complex_to_arg_0 = blocks.complex_to_arg(1)
        self.SekizKanalFFT_0 = SekizKanalFFT()

        ##################################################
        # Connections
        ##################################################
        self.connect((self.SekizKanalFFT_0, 0), (self.blocks_complex_to_mag_0_0, 0))    
        self.connect((self.SekizKanalFFT_0, 0), (self.blocks_file_sink_3, 0))    
        self.connect((self.SekizKanalFFT_0, 0), (self.blocks_keep_m_in_n_0, 0))    
        self.connect((self.SekizKanalFFT_0, 1), (self.blocks_keep_m_in_n_0_0, 0))    
        self.connect((self.SekizKanalFFT_0, 4), (self.blocks_null_sink_0, 0))    
        self.connect((self.SekizKanalFFT_0, 2), (self.blocks_null_sink_0_0_0, 0))    
        self.connect((self.SekizKanalFFT_0, 3), (self.blocks_null_sink_0_0_1, 0))    
        self.connect((self.SekizKanalFFT_0, 6), (self.blocks_null_sink_1, 0))    
        self.connect((self.SekizKanalFFT_0, 7), (self.blocks_null_sink_2, 0))    
        self.connect((self.SekizKanalFFT_0, 5), (self.blocks_null_sink_3, 0))    
        self.connect((self.blocks_complex_to_arg_0, 0), (self.blocks_file_sink_1, 0))    
        self.connect((self.blocks_complex_to_mag_0, 0), (self.blocks_file_sink_2, 0))    
        self.connect((self.blocks_complex_to_mag_0_0, 0), (self.qtgui_time_sink_x_0, 0))    
        self.connect((self.blocks_file_source_0, 0), (self.SekizKanalFFT_0, 0))    
        self.connect((self.blocks_keep_m_in_n_0, 0), (self.blocks_complex_to_arg_0, 0))    
        self.connect((self.blocks_keep_m_in_n_0, 0), (self.blocks_complex_to_mag_0, 0))    
        self.connect((self.blocks_keep_m_in_n_0, 0), (self.blocks_multiply_conjugate_cc_0, 1))    
        self.connect((self.blocks_keep_m_in_n_0_0, 0), (self.blocks_multiply_conjugate_cc_0, 0))    
        self.connect((self.blocks_multiply_conjugate_cc_0, 0), (self.blocks_file_sink_2_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()


    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)


def main(top_block_cls=top_block, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
