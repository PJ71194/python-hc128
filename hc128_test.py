import unittest
import hc128

class TestHc128(unittest.TestCase):

  def test_sample1(self):
    hc128.init("00000000000000000000000000000000", "00000000000000000000000000000000")
    hc128.i = 0
    out = "82001573a003fd3b7fd72ffb0eaf63aac62f12deb629dca72785a66268ec758b1edb36900560898178e0ad009abf1f491330dc1c246e3d6cb264f6900271d59c"
    for i in range(0, 8):
      self.assertEquals(out[i*8:i*8 + 8], hc128.keygen())

  def test_sample2(self):
    hc128.init("0558ABFE51A4F74A9DF04396E93C8FE2", "00000000000000000000000000000000")
    hc128.i = 0
    out = "54182309bd782dee44fb59b0ec6949202b372af8d715271a96d87867e65a067fa5e52b455b76d400537b5d47c4ac318eee4c2abe29f56107c213071c85828605"
    for i in range(0, 8):
      self.assertEquals(out[i*8:i*8 + 8], hc128.keygen())

  def test_sample3(self):
    hc128.init("0F62B5085BAE0154A7FA4DA0F34699EC", "288FF65DC42B92F960C72E95FC63CA31")
    hc128.i = 0
    out = "1cd8aeddfe52e217e835d0b7e84e2922d04b1adbca53c4522b1aa604c42856a90af83e2614bce65c0aecabdd8975b55700d6a26d52fff0888da38f1de20b77b7"
    for i in range(0, 8):
      self.assertEquals(out[i*8:i*8 + 8], hc128.keygen())

if __name__ == '__main__':
  unittest.main()
