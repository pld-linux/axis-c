# TODO:
# - look at examples. maybe package it, or simply include in -examples?
%define		fversion	%(echo %{version} |tr . -)
Summary:	WebServices - Axis
Summary(pl):	WebServices - Axis
Name:		axis-c
Version:	1.2
Release:	1
License:	Apache Software License
Group:		Libraries
Source0:	http://www.apache.org/dist/ws/axis-c/source/linux/%{name}-src-%{fversion}-linux.tar.gz
# Source0-md5:	9c68ba2f2d8029aed0694881bc2f491b
URL:		http://ws.apache.org/axis/
BuildRequires:	apr-util-devel
BuildRequires:	apr-devel
BuildRequires:	apache-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	expat-devel
BuildRequires:	xerces-c-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Apache Axis is an implementation of the SOAP ("Simple Object Access
Protocol") submission to W3C.

%description -l pl
Apache Axis jest implementacją SOAP ("Simple Object Access Protocol")
przekazaną do W3C.

%package devel
Summary:	WebServices - Axis - development files
Summary(pl):	WebServices - Axis - pliki nagłówkowe
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
WebServices - Axis - development files.

%description devel -l pl
WebServices - Axis - pliki nagłówkowe.

%package static
Summary:	WebServices - Axis - static files
Summary(pl):	WebServices - Axis - biblioteka statyczna
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
WebServices - Axis - static files.

%description static -l pl
WebServices - Axis - biblioteka statyczna.

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
%{_libdir}/lib*.la
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/axis

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
