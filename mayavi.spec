
Summary: A powerful scientific data visualizer for Python
Name: mayavi
Version: 1.5
Release: %mkrel 5
Source0: http://ovh.dl.sourceforge.net/sourceforge/mayavi/MayaVi-%{version}.tar.bz2
License: BSD
Group: Sciences/Other
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
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
python setup.py install --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)



