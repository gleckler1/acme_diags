import sys
from setuptools import find_packages, setup



data_files = [
    (sys.prefix + '/share/acme_diags/zonal_mean_xy',
     ['acme_diags/driver/zonal_mean_xy_AMWG.json',
      'acme_diags/driver/zonal_mean_xy_ACME.json',
      'acme_diags/plot/vcs/plot_set_3.json'
     ]),
    (sys.prefix + '/share/acme_diags/zonal_mean_2d',
     ['acme_diags/driver/zonal_mean_2d_AMWG.json',
      'acme_diags/driver/zonal_mean_2d_ACME.json',
      'acme_diags/plot/vcs/plot_set_4.json',
      'acme_diags/plot/vcs/plot_set_4_new.json'
     ]),
    (sys.prefix + '/share/acme_diags/lat_lon',
     ['acme_diags/driver/lat_lon_AMWG.json',
      'acme_diags/driver/lat_lon_ACME.json',
      'acme_diags/plot/vcs/plot_set_5_new.json',
      'acme_diags/plot/vcs/plot_set_5.json'
     ]),
    (sys.prefix + '/share/acme_diags/polar',
     ['acme_diags/driver/polar_AMWG.json',
      'acme_diags/driver/polar_ACME.json',
      'acme_diags/plot/vcs/plot_set_7_new.json',
      'acme_diags/plot/vcs/plot_set_7.json'
     ]),
    (sys.prefix + '/share/acme_diags/cosp_histogram',
     ['acme_diags/driver/cosp_histogram_AMWG.json',
      'acme_diags/driver/cosp_histogram_ACME.json'
     ]),
    (sys.prefix + '/share/acme_diags',
     ['acme_diags/driver/acme_ne30_ocean_land_mask.nc',
      'docs/ACME_Logo.png'
     ]),
    (sys.prefix + '/share/acme_diags/colormaps',
     ['acme_diags/plot/colormaps/precip_diff_12lev.rgb',
      'acme_diags/plot/colormaps/temp_diff_18lev.rgb',
      'acme_diags/plot/colormaps/WhiteBlueGreenYellowRed.rgb'
     ])
]

setup(
    name="acme_diags",
    version="1.0.0",
    author="Chengzhu (Jill) Zhang, Zeshawn Shaheen",
    author_email="aims@llnl.gov",
    description="ACME Diagnostics.",
    scripts=["acme_diags/acme_diags_driver.py"],
    packages=find_packages(exclude=["*.test", "*.test.*", "test.*", "test"]),
    data_files=data_files
)
