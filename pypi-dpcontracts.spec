#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-dpcontracts
Version  : 0.6.0
Release  : 28
URL      : https://files.pythonhosted.org/packages/aa/e2/cad64673297a634a623808045d416ed85bad1c470ccc99e0cdc7b13b9774/dpcontracts-0.6.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/aa/e2/cad64673297a634a623808045d416ed85bad1c470ccc99e0cdc7b13b9774/dpcontracts-0.6.0.tar.gz
Summary  : A simple implementation of contracts for Python.
Group    : Development/Tools
License  : LGPL-2.1
Requires: pypi-dpcontracts-python = %{version}-%{release}
Requires: pypi-dpcontracts-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
Introduction
        ============
        This module provides a collection of decorators that makes it easy to
        write software using contracts.
        
        Contracts are a debugging and verification tool.  They are declarative
        statements about what states a program must be in to be considered
        "correct" at runtime.  They are similar to assertions, and are verified
        automatically at various well-defined points in the program.  Contracts can
        be specified on functions and on classes.
        
        Contracts serve as a form of documentation and a way of formally
        specifying program behavior.  Good practice often includes writing all of
        the contracts first, with these contract specifying the exact expected
        state before and after each function or method call and the things that
        should always be true for a given class of object.

%package python
Summary: python components for the pypi-dpcontracts package.
Group: Default
Requires: pypi-dpcontracts-python3 = %{version}-%{release}

%description python
python components for the pypi-dpcontracts package.


%package python3
Summary: python3 components for the pypi-dpcontracts package.
Group: Default
Requires: python3-core
Provides: pypi(dpcontracts)

%description python3
python3 components for the pypi-dpcontracts package.


%prep
%setup -q -n dpcontracts-0.6.0
cd %{_builddir}/dpcontracts-0.6.0
pushd ..
cp -a dpcontracts-0.6.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656406879
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
