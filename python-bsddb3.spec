Name:           python-bsddb3
Version:        6.2.9
Release:        2
Summary:        Python 3 bindings for BerkleyDB
Group:          Development/Python
License:        BSD
URL:            https://pypi.python.org/pypi/bsddb3/
Source0:        https://pypi.python.org/packages/source/b/bsddb3/bsddb3-%{version}.tar.gz

Requires:       python
BuildRequires:  pkgconfig(python)
BuildRequires:  python3dist(setuptools)
#BuildRequires:  db-devel
# Max 53 is supported, do not use greater version.
BuildRequires:  db53-devel
BuildRequires:  glibc
%rename python3-bsddb3

%description
This package contains Python wrappers for Berkeley DB, the Open Source embedded
database system. The Python wrappers allow you to store Python string objects 
of any length.

%prep
%setup -q -n bsddb3-%{version}

%build
%py_build

%install
%py3_install

%files 
%doc ChangeLog PKG-INFO README.txt LICENSE.txt
%{python3_sitearch}/bsddb3/
%{python3_sitearch}/bsddb3-%{version}-py*.*.egg-info
%{_includedir}/python*.*/bsddb3/bsddb.h
