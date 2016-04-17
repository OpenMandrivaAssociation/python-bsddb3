Name:           python3-bsddb3
Version:        6.1.1
Release:        %mkrel 1
Summary:        Python 3 bindings for BerkleyDB
Group:          Development/Python

License:        BSD
URL:            https://pypi.python.org/pypi/bsddb3/
Source0:        https://pypi.python.org/packages/source/b/bsddb3/bsddb3-%{version}.tar.gz

Requires:       python(abi) >= 3.0
BuildRequires:  python3-devel
BuildRequires:  db-devel

%description
This package contains Python wrappers for Berkeley DB, the Open Source embedded
database system. The Python wrappers allow you to store Python string objects 
of any length.

%prep
%setup -q -n bsddb3-%{version}

%build
%__python3 setup.py build

%install
%__python3 setup.py install --skip-build --root=%{buildroot}
# Get rid of unneeded header
rm -f %{buildroot}%{_includedir}/python3.?m/bsddb3/bsddb.h
# Make all scripts executable
chmod 0755 %{buildroot}%{python3_sitearch}/bsddb3/{dbshelve.py,tests/test_dbtables.py}

%check
#{__python3} test.py

%files 
%doc ChangeLog PKG-INFO README.txt LICENSE.txt
%{python3_sitearch}/bsddb3/
%{python3_sitearch}/bsddb3-%{version}-py3.?.egg-info
