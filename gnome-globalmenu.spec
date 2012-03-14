%global date 20120314
%global gitcommit e4502d33b2
%global realver 0.9

Name:           gnome-globalmenu
Version:        %{realver}.%{date}git%{gitcommit}
Release:        1%{?dist}
Summary:        Global Menu for GNOME

License:        GPLv2 and LGPLv2
URL:            http://code.google.com/p/gnome2-globalmenu/
Source0:        %{name}-%{realver}.git.tar.xz
Source100:      README.RFRemix

BuildRequires:  vala-devel
BuildRequires:  gtk3-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk2-devel
BuildRequires:  autogen
BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  intltool
BuildRequires:  glibc-devel
BuildRequires:  libtool


%description
GNOME Global Menu is a centralized menu bar for all windows on a particular
screen/session. This package extends GTK and gnome panel so that Global Menu
can be enabled on all GTK applications.
The Gtk Plugin Module of Global Menu adds global menu feature to any GTK
applications on the fly without the need of modifying the source code.
gnome-applet-globalmenu or xfce-globalmenu-plugin should also be installed
depending on the desktop environment.

%prep
%setup -q -n %{name}-%{realver}.git


%build
autoreconf --force --install --verbose
./autogen.sh --prefix=/usr
make
cp %{SOURCE100} .


%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT GTK2_MODULES_DIR=%{_libdir}/gtk-2.0/modules GTK3_MODULES_DIR=%{_libdir}/gtk-3.0/modules GLIB_COMPILE_SCHEMAS=/bin/true install

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/profile.d/
mv $RPM_BUILD_ROOT/usr/etc/profile.d/globalmenu.sh $RPM_BUILD_ROOT%{_sysconfdir}/profile.d/globalmenu.sh
rm -rf $RPM_BUILD_ROOT/usr/etc/

ln -sfv /%{_libdir}/gtk-2.0/modules/libglobalmenu-gtk2.so $RPM_BUILD_ROOT%{_libdir}/gtk-2.0/modules/libglobalmenu-gtk.so
sed -i 's/3\.2\.0/3\.2/' $RPM_BUILD_ROOT/usr/share/gnome-shell/extensions/GlobalMenu@globalmenu.org/metadata.json

rm -f $RPM_BUILD_ROOT/%{_libdir}/gtk-2.0/modules/libglobalmenu-gtk2.la
rm -f $RPM_BUILD_ROOT/%{_libdir}/gtk-3.0/modules/libglobalmenu-gtk.la
rm -rf $RPM_BUILD_ROOT/usr/share/doc/gnome-globalmenu

%post
glib-compile-schemas /usr/share/glib-2.0/schemas

%files
%defattr(-,root,root,-)
%{_bindir}/gnome-globalmenu-manager
%{_sysconfdir}/profile.d/globalmenu.sh
%{_libdir}/gtk-2.0/modules/libglobalmenu-gtk.so
%{_libdir}/gtk-2.0/modules/libglobalmenu-gtk2.so
%{_libdir}/gtk-3.0/modules/libglobalmenu-gtk.so
%{_datadir}/dbus-1/services/org.globalmenu.manager.service
%{_datadir}/glib-2.0/schemas/org.globalmenu.gschema.xml
%{_datadir}/gnome-shell/extensions/GlobalMenu@globalmenu.org/*
%{_mandir}/man1/gnome-globalmenu.1.gz
%doc AUTHORS README ChangeLog COPYING README.GNOME README.RFRemix


%changelog
* Sun Mar 11 2012 Vasiliy N. Glazov <vascom2@gmail.com> - 0.9-2.R
- added globalmenu.sh for automatic load

* Sun Mar 11 2012 Vasiliy N. Glazov <vascom2@gmail.com> - 0.9-1.R
- initial release for Gnome 3
