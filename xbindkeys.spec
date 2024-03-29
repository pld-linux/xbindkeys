#
# Conditional build:
%bcond_without	guile	# disable scheme/guile configuration file style
#
Summary:	Binds keys or mouse buttons to shell commands under X
Summary(pl.UTF-8):	Przypisywanie poleceniom powłoki przycisków myszy lub klawiatury pod X
Name:		xbindkeys
Version:	1.8.7
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://www.nongnu.org/xbindkeys/%{name}-%{version}.tar.gz
# Source0-md5:	b5e1a9668ba13ff8673836d1d965d951
URL:		http://www.nongnu.org/xbindkeys/xbindkeys.html
BuildRequires:	autoconf >= 2.59-9
BuildRequires:	automake
%{?with_guile:BuildRequires:	guile-devel}
BuildRequires:	libtool
BuildRequires:	xorg-lib-libX11-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xbindkeys is a program that allows you to launch shell commands with
your keyboard or mouse under X11. It links commands to keys or mouse
buttons using a simple configuration file, and is independant of the
window manager. 

%description -l pl.UTF-8
xbindkeys jest programem, który pozwala na uruchamianie poleceń
powłoki przy użyciu klawiatury lub myszki pod X11. Xbindkeys
przypisuje polecenia przyciskom za pomocą prostego pliku
konfiguracyjnego, niezależnie od zarządcy okien. Pozwala na
przechwytywanie takich przycisków jak POWER czy WAKE na klawiaturze.

%package xbindkeys_show
Summary:	Program to show the grabbing keys used in xbindkeys
Summary(pl.UTF-8):	Program pokazujący przyciski obsługiwane przez xbindkeys
Group:		X11/Applications
Requires:	%{name}
Requires:	tk

%description xbindkeys_show
xbindkeys_show is a Tk program that shows the grabbing keys used in
xbindkeys.

%description xbindkeys_show -l pl.UTF-8
xbindkeys_show jest programem w Tk, który pokazuje przyciski
obsługiwane aktualnie przez xbindkeys.

%prep
%setup -q

touch config.rpath

%build
rm -f aclocal.m4
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-x \
	%{!?with_guile: --disable-guile}

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
%{_mandir}/man1/xbindkeys.1*

%files xbindkeys_show
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xbindkeys_show
%{_mandir}/man1/xbindkeys_show.1*
