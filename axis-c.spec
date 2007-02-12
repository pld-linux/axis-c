# TODO:
# - look at examples. maybe package it, or simply include in -examples?
%define		fversion	%(echo %{version} |tr . -)
Summary:	Axis - implementation of the SOAP submission to W3C
Summary(pl.UTF-8):	Axis - implementacja protokołu SOAP przekazanego do W3C
Name:		axis-c
Version:	1.2
Release:	2
License:	Apache Software License
Group:		Libraries
Source0:	http://www.apache.org/dist/ws/axis-c/source/linux/%{name}-src-%{fversion}-linux.tar.gz
# Source0-md5:	9c68ba2f2d8029aed0694881bc2f491b
URL:		http://ws.apache.org/axis/
BuildRequires:	apache-devel
BuildRequires:	apr-devel
BuildRequires:	apr-util-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	expat-devel
BuildRequires:	libtool
BuildRequires:	xerces-c-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Apache Axis is an implementation of the SOAP ("Simple Object Access
Protocol") submission to W3C.

%description -l pl.UTF-8
Apache Axis jest implementacją SOAP ("Simple Object Access Protocol")
przekazaną do W3C.

%package devel
Summary:	Development files for Axis libraries
Summary(pl.UTF-8):	Pliki programistyczne bibliotek Axis
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Development files for Axis libraries.

%description devel -l pl.UTF-8
Pliki programistyczne bibliotek Axis.

%package static
Summary:	Static Axis libraries
Summary(pl.UTF-8):	Statyczne biblioteki Axis
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Axis libraries.

%description static -l pl.UTF-8
Statyczne biblioteki Axis.

%prep
%setup -q -n %{name}-src-%{fversion}-linux
rm -rf include/expat
ln -sf %{_includedir} include/expat
ln -sf %{_includedir}/apache/* %{_includedir}/apr/* include/apache2_0

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
CFLAGS="%{rpmcflags} -I`pwd`/include -I%{_includedir}/apr-util -I%{_includedir}/apr"
CXXFLAGS="%{rpmcflags} -I`pwd`/include -I%{_includedir}/apr-util -I%{_includedir}/apr"
%configure
%{__make} \
	AXISCPP_HOME="`pwd`"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_includedir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -r include/axis $RPM_BUILD_ROOT%{_includedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE NOTICE docs/TODO.txt docs/linux docs/*.html
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%doc docs/apidocs/html docs/RFC/* docs/QnA/*
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/axis

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
