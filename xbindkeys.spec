Summary:	Binds keys or mouse buttons to shell commands under X
Summary(pl.UTF-8):	Przypisywanie poleceniom powłoki przycisków myszy lub klawiatury pod X
Name:		xbindkeys
Version:	1.8.2
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://hocwp.free.fr/xbindkeys/%{name}-%{version}.tar.gz
# Source0-md5:	ad1abd56e758bc108493ad0e5b862ad3
URL:		http://hocwp.free.fr/xbindkeys/xbindkeys.html
BuildRequires:	autoconf >= 2.59-9
BuildRequires:	automake
BuildRequires:	guile-devel
BuildRequires:	libtool
BuildRequires:	xorg-lib-libX11-devel
Requires:	tk
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xbindkeys is a program that allows you to launch shell commands with
your keyboard or mouse under X11. It links commands to keys or mouse
buttons using a simple configuration file, and is independant of the
window manager. XMMS panel applet for the KDE panel (kicker). It is
used to be able

%description -l pl.UTF-8
xbindkeys jest programem, który pozwala na uruchamianie poleceń
powłoki przy użyciu klawiatury lub myszki pod X11. Xbindkeys
przypisuje polecenia przyciskom za pomocą prostego pliku
konfiguracyjnego, niezależnie od zarządcy okien. Pozwala na
przechwytywanie takich przycisków jak POWER czy WAKE na klawiaturze.

%prep
%setup -q

%build
rm -f aclocal.m4
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
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
