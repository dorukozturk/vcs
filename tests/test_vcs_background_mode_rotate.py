import basevcstest
import vcs
import numpy

class TestVCSBackgroundModeRotate(basevcstest.VCSBaseTest):
	def testBackgroundModeRotate(self):

		data = numpy.sin(numpy.arange(100))
		data = numpy.reshape(data, (10, 10))

		self.x = vcs.init()
		self.x.plot(data, bg=self.bg)
		self.assertEqual(self.x.orientation(), "landscape", "Default canvas orientation failed")
		c = self.x.canvasinfo()
		self.assertEqual(c['width'], 814, "Default canvas width failed")
		self.assertEqual(c['height'], 606, "Default canvas height failed")

		self.x.clear()
		self.x.portrait()
		self.x.plot(data, bg=self.bg)
		self.assertEqual( self.x.orientation(), "portrait", "Portrait canvas orientation failed")
		c = self.x.canvasinfo()
		self.assertEqual( c['width'], 606, "Portrait canvas width failed")
		self.assertEqual( c['height'], 814, "Portrait canvas height failed")

		self.x.clear()
		self.x.landscape()
		self.x.plot(data, bg=self.bg)
		self.assertEqual( self.x.orientation(), "landscape", "Landscape canvas orientation failed")
		c = self.x.canvasinfo()
		self.assertEqual( c['width'], 814, "Landscape canvas width failed")
		self.assertEqual( c['height'], 606, "Landscape canvas height failed")

		self.x.clear()
		self.x.landscape()
		self.x.plot(data, bg=self.bg)
		self.assertEqual( self.x.orientation(), "landscape", "Landscape canvas orientation failed")
		c = self.x.canvasinfo()
		self.assertEqual( c['width'], 814, "Landscape canvas width failed")
		self.assertEqual( c['height'], 606, "Landscape canvas height failed")

		self.x.clear()
		self.x.portrait()
		self.x.plot(data, bg=self.bg)
		self.assertEqual( self.x.orientation(), "portrait", "Portrait canvas orientation failed")
		c = self.x.canvasinfo()
		self.assertEqual( c['width'], 606, "Portrait canvas width failed")
		self.assertEqual( c['height'], 814, "Portrait canvas height failed")
