Summary:	Binds keys or mouse buttons to shell commands under X.
Summary(pl):	TODO
Name:		xbindkeys
Version:	1.5.4
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://hocwp.free.fr/xbindkeys/%{name}-%{version}.tar.gz
URL:		http://hocwp.free.fr/xbindkeys/xbindkeys.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	XFree86-devel
Requires:	tk
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xbindkeys is a program that allows you to launch shell commands with
your keyboard or mouse under X. It links commands to keys or mouse
buttons using a simple configuration file, and is independant of the
window manager. XMMS panel applet for the KDE panel (kicker). It is
used to be able

%description -l pl
TODO

%prep
%setup -q

%build
rm -f missing aclocal.m4
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with-x

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/xbindkeys
%attr(755,root,root) %{_bindir}/xbindkeys_show
%{_mandir}/man1/xbindkeys*
