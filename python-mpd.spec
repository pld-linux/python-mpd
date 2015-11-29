%define		module	mpd
Summary:	Python MPD client library
Summary(pl.UTF-8):	Biblioteka klienta MPD dla Pythona
Name:		python-%{module}
Version:	0.3.0
Release:	2
License:	GPL
Group:		Development/Languages/Python
Source0:	http://pypi.python.org/packages/source/p/python-mpd/%{name}-%{version}.tar.bz2
# Source0-md5:	cfd4b907ba8ef33ff79bd7cbc16b25c0
URL:		http://jatreuman.indefero.net/p/python-mpd/
BuildRequires:	rpmbuild(macros) >= 1.710
BuildRequires:	python
BuildRequires:	python-devel >= 1:2.3
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An MPD (Music Player Daemon) client library written in pure Python.

%description -l pl.UTF-8
Bilioteka klienta MPD (Music Player Daemon) napisana w czystym
Pythonie.

%prep
%setup -q -n python-mpd-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py_sitescriptdir}/mpd.py[co]
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/python_mpd-*.egg-info
%endif
