%define		module	mpd

Summary:	Python MPD client library.
Summary(pl.UTF-8):	 Biblioteka klienta MPD dla Pythona
Name:		python-%{module}
Version:	0.2.1
Release:	1
License:	GPL
Group:		Development/Languages/Python
Source0:	http://pypi.python.org/packages/source/p/python-mpd/%{name}-%{version}.tar.bz2
# Source0-md5:	4b7eafe3de91a7ab14099503f6691db1
URL:		http://pypi.python.org/pypi/python-mpd/
BuildRequires:	python
BuildRequires:	python-devel >= 1:2.3
%pyrequires_eq	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An MPD (Music Player Daemon) client library written in pure Python.

%description -l pl.UTF-8
Bilioteka klienta MPD (Music Player Daemon) napisana w czystym Python'ie.

%prep
%setup -q -n python-mpd-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install \
	--root=$RPM_BUILD_ROOT --optimize=2

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py_sitescriptdir}/mpd.py
%{py_sitescriptdir}/mpd.py[co]
%{py_sitescriptdir}/python_mpd-%{version}-py2.5.egg-info
