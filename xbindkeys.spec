Summary:	Binds keys or mouse buttons to shell commands under X
Summary(pl):	Przypisywanie poleceniom pow³oki przycisków myszy lub klawiatury pod X
Name:		xbindkeys
Version:	1.7.2
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://hocwp.free.fr/xbindkeys/%{name}-%{version}.tar.gz
# Source0-md5:	7aead9049d972221b879f22718528690
URL:		http://hocwp.free.fr/xbindkeys/xbindkeys.html
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	guile-devel
Requires:	tk
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xbindkeys is a program that allows you to launch shell commands with
your keyboard or mouse under X11. It links commands to keys or mouse
buttons using a simple configuration file, and is independant of the
window manager. XMMS panel applet for the KDE panel (kicker). It is
used to be able

%description -l pl
xbindkeys jest programem, który pozwala na uruchamianie poleceñ
pow³oki przy u¿yciu klawiatury lub myszki pod X11. Xbindkeys
przypisuje polecenia przyciskom za pomoc± prostego pliku
konfiguracyjnego, niezale¿nie od zarz±dcy okien. Pozwala na
przechwytywanie takich przycisków jak POWER czy WAKE na klawiaturze.

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

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/xbindkeys
%attr(755,root,root) %{_bindir}/xbindkeys_show
%{_mandir}/man1/xbindkeys*
