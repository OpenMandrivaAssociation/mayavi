
Summary: A powerful scientific data visualizer for Python
Name: mayavi
Version: 1.5
Release: 9
Source0: http://ovh.dl.sourceforge.net/sourceforge/mayavi/MayaVi-%{version}.tar.bz2
License: BSD
Group: Sciences/Other
BuildArch: noarch
Url: http://mayavi.sourceforge.net
Requires: tkinter, python-vtk
BuildRequires: python-devel

%description
 MayaVi is a free, easy to use scientific data visualizer. It is written in
Python and uses the amazing Visualization Toolkit (VTK) for the graphics. It
provides a GUI written using  Tkinter. MayaVi is free and distributed under the
conditions of the  BSD license. It is also cross platform and should run on any
platform where both Python and VTK are available (which is almost any *nix, Mac
OSX or Windows).

%prep
%setup -n MayaVi-%version

%build
python setup.py build

%install
PYTHONDONTWRITEBYTECODE= python setup.py install --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%files -f INSTALLED_FILES
%defattr(-,root,root)





%changelog
* Fri Sep 04 2009 Thierry Vignaud <tvignaud@mandriva.com> 1.5-8mdv2010.0
+ Revision: 429978
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.5-7mdv2009.0
+ Revision: 241020
- rebuild
- fix no-buildroot-tag
- kill re-definition of %%buildroot on Pixel's request

* Mon Aug 27 2007 GaÃ«tan Lehmann <glehmann@mandriva.org> 1.5-5mdv2008.0
+ Revision: 72202
- rebuild


* Fri Dec 22 2006 GaÃ«tan Lehmann <glehmann@mandriva.org> 1.5-4mdv2007.0
+ Revision: 101831
- rebuild for new python

* Thu Aug 10 2006 GaÃ«tan Lehmann <glehmann@mandriva.org> 1.5-3mdv2007.0
+ Revision: 55095
- rebuild
- Import mayavi

* Fri Oct 21 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.5-2mdk
- Fix BuildRequires

* Thu Oct 20 2005 Gaetan Lehmann <gaetan.lehmann@jouy.inra.fr> 1.5-1mdk
- New release 1.5

* Tue Jun 21 2005 <gaetan.lehmann@jouy.inra.fr> 1.4-1mdk
- first contrib

