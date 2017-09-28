from __future__ import unicode_literals
import numpy as np
from numpy import ma
from matplotlib import scale as mscale
from matplotlib import transforms as mtransforms
from matplotlib.ticker import Formatter, FixedLocator
from matplotlib import rcParams
rcParams['axes.axisbelow'] = False
class MercatorLatitudeScale(mscale.ScaleBase):
    name = 'oneoverx'
    def __init__(self, axis, **kwargs):
      pass
    def get_transform(self):
        return self.MercatorLatitudeTransform()

    def set_default_locators_and_formatters(self, axis):
        class DegreeFormatter(Formatter):
            def __call__(self, x, pos=None):
                # \u00b0 : degree symbol
                return x

        axis.set_major_locator(FixedLocator(
            np.arange(10, 90, 10)))
        axis.set_major_formatter(DegreeFormatter())
        axis.set_minor_formatter(DegreeFormatter())
    """
    def limit_range_for_scale(self, vmin, vmax, minpos):
        
        Override to limit the bounds of the axis to the domain of the
        transform.  In the case of Mercator, the bounds should be
        limited to the threshold that was passed in.  Unlike the
        autoscaling provided by the tick locators, this range limiting
        will always be adhered to, whether the axis range is set
        manually, determined automatically or changed through panning
        and zooming.
        
        return vmin, vmax
    """
    class MercatorLatitudeTransform(mtransforms.Transform):
        input_dims = 1
        output_dims = 1
        is_separable = True
        def __init__(self):
            mtransforms.Transform.__init__(self)
            #self.thresh = thresh

        def transform_non_affine(self, a):
          return (10000000/a)
        def inverted(self):
            return MercatorLatitudeScale.InvertedMercatorLatitudeTransform()
    class InvertedMercatorLatitudeTransform(mtransforms.Transform):
        input_dims = 1
        output_dims = 1
        is_separable = True
        def __init__(self):
            mtransforms.Transform.__init__(self)
        def transform_non_affine(self, a):
            return (10000000/a)
        def inverted(self):
            return MercatorLatitudeScale.MercatorLatitudeTransform()
# Now that the Scale class has been defined, it must be registered so
# that ``matplotlib`` can find it.
mscale.register_scale(MercatorLatitudeScale)
"""
if __name__ == '__main__':
  import matplotlib.pyplot as plt
  x = np.arange(1,10)
  y = x*2
  plt.plot(x, y, '-', lw=1)
  plt.gca().set_xscale('oneoverx')
  
  plt.xlabel('Longitude')
  plt.ylabel('Latitude')
  plt.title('Mercator: Projection of the Oppressor')
  plt.grid(True)

  plt.show()



if __name__ == '__main__':
    import matplotlib.pyplot as plt

    t = np.arange(10, 180.0, 0.1)
    s = t/2.

    plt.plot(t, s, '-', lw=2)
    plt.gca().set_yscale('oneoverx')

    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.title('Mercator: Projection of the Oppressor')
    plt.grid(True)

    plt.show()
"""