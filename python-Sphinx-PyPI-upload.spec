#
# Conditional build:
# %bcond_without	tests	# do not perform "make test"

%define 	module	Sphinx-PyPI-upload
Summary:	setuptools command for uploading Sphinx documentation to PyPI
Summary(pl.UTF-8):	komenda setuptools do publikowana dokumentacji Sphinx na PyPI
Name:		python-%{module}
Version:	0.2.1
Release:	2
License:	BSD-3
Group:		Development/Languages/Python
Source0:	http://pypi.python.org/packages/source/S/%{module}/%{module}-%{version}.tar.gz
# Source0-md5:	b9f1df5c8443197e4d49abbba1cfddc4
URL:		https://bitbucket.org/jezdez/sphinx-pypi-upload/
BuildRequires:	python-devel
BuildRequires:	python-distribute
BuildRequires:	rpm-pythonprov
# remove BR: python-devel for 'noarch' packages.
# if py_postclean is used
BuildRequires:	rpmbuild(macros) >= 1.219
#Requires:		python-libs
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
setuptools command for uploading Sphinx documentation to PyPI

%description -l pl.UTF-8
komenda setuptools do publikowana dokumentacji Sphinx na PyPI

%prep
%setup -q -n %{module}-%{version}

%build
%py_build

# %{?with_tests:%{__python} setup.py test}

%install
rm -rf $RPM_BUILD_ROOT
%py_install

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{py_sitescriptdir}/*.py[co]
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/Sphinx_PyPI_upload-*.egg-info
%endif
