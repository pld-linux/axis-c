%define		fversion	%(echo %{version} |tr . -)
Summary:	WebServices - Axis
Summary(pl):	WebServices - Axis
Name:		axis-c
Version:	1.2
Release:	0.1
License:	Apache Software License
Group:		Development/Libraries
Source0:	http://www.apache.org/dist/ws/axis-c/source/linux/%{name}-src-%{fversion}-linux.tar.gz
# Source0-md5:	9c68ba2f2d8029aed0694881bc2f491b
URL:		http://ws.apache.org/axis/
BuildRequires:	apr-util-devel
BuildRequires:	apr-devel
BuildRequires:	apache-devel
BuildRequires:	expat-devel
BuildRequires:	xerces-c-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Apache Axis is an implementation of the SOAP ("Simple Object Access
Protocol") submission to W3C.

%description -l pl
Apache Axis jest implementacj± SOAP ("Simple Object Access Protocol")
przekazan± do W3C.

%package devel
Summary:	WebServices - Axis - development files
Summary(pl):	WebServices - Axis - pliki nag³ówkowe
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
WebServices - Axis - development files.

%description devel -l pl
WebServices - Axis - pliki nag³ówkowe.

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

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%{_libdir}/lib*.la
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/axis

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
