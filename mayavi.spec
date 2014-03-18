Summary:	A powerful scientific data visualizer for Python
Name:		mayavi
Version:	1.5
Release:	10
License:	BSD
Group:		Sciences/Other
Url:		http://mayavi.sourceforge.net
Source0:	http://ovh.dl.sourceforge.net/sourceforge/mayavi/MayaVi-%{version}.tar.bz2
BuildRequires:	pkgconfig(python)
Requires:	python-vtk
Requires:	tkinter
BuildArch:	noarch

%description
MayaVi is a free, easy to use scientific data visualizer. It is written in
Python and uses the amazing Visualization Toolkit (VTK) for the graphics. It
provides a GUI written using  Tkinter. MayaVi is free and distributed under the
conditions of the  BSD license. It is also cross platform and should run on any
platform where both Python and VTK are available (which is almost any *nix, Mac
OSX or Windows).

%files -f INSTALLED_FILES

#----------------------------------------------------------------------------

%prep
%setup -n MayaVi-%{version}

%build
python setup.py build

%install
PYTHONDONTWRITEBYTECODE= python setup.py install --root=%{buildroot} --record=INSTALLED_FILES

