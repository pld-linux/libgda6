#
# Conditional build:
%bcond_without	apidocs		# API documentation
%bcond_without	glade		# Glade catalog
%bcond_without	static_libs	# static libraries build
%bcond_without	vala		# Vala APIs and GdaData C library
# - database plugins:
%bcond_with	db		# BerkeleyDB plugin (broken, disabled in sources)
%bcond_with	dbsql		# BerkeleyDB SQL plugin (not supported in meson buildsystem)
%bcond_with	firebird	# Firebird plugins (not supported in meson buildsystem)
%bcond_with	jdbc		# JDBC plugin (disabled in sources)
%bcond_without	ldap		# LDAP plugin
%bcond_with	mdb		# MDB plugin (not supported in meson buildsystem)
%bcond_without	mysql		# MySQL plugin
%bcond_with	oci		# Oracle DB plugin (not supported in meson buildsystem)
%bcond_without	pgsql		# PostgreSQL plugin
%bcond_without	sqlcipher	# SQLcipher plugin

%ifnarch i486 i586 i686 pentium3 pentium4 athlon %{x8664}
%undefine	with_jdbc
%endif

Summary:	GNU Data Access library
Summary(pl.UTF-8):	Biblioteka GNU Data Access
Name:		libgda6
Version:	6.0.0
Release:	6
License:	LGPL v2+/GPL v2+
Group:		Libraries
Source0:	https://download.gnome.org/sources/libgda/6.0/libgda-%{version}.tar.xz
# Source0-md5:	2e059e57b0620fb23fc74f3d2bd0fd1f
Patch0:		%{name}-web.patch
Patch1:		%{name}-soname.patch
Patch2:		meson0.61.patch
Patch3:		types.patch
Patch4:		vapi-deps.patch
URL:		https://www.gnome-db.org/
%{?with_firebird:BuildRequires:	Firebird-devel}
BuildRequires:	autoconf >= 2.68
BuildRequires:	automake >= 1:1.11.1
%{?with_db:BuildRequires:	db-devel >= 4.7}
%{?with_dbsql:BuildRequires:	db-sql-devel >= 4.7}
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gdk-pixbuf2-devel >= 2.0
BuildRequires:	gettext-tools
# pkgconfig(gladeui-2.0)
%{?with_glade:BuildRequires:	glade-devel >= 3.0}
BuildRequires:	glib2-devel >= 1:2.32.0
BuildRequires:	glibc-misc
BuildRequires:	gobject-introspection-devel >= 1.30.0
BuildRequires:	goocanvas2-devel >= 2.0
BuildRequires:	graphviz-devel
BuildRequires:	gtk+3-devel >= 3.0.0
BuildRequires:	gtk-doc >= 1.14
BuildRequires:	gtksourceview3-devel >= 3.0
BuildRequires:	intltool >= 0.40.6
BuildRequires:	iso-codes
%{?with_jdbc:BuildRequires:	jdk >= 1.5}
BuildRequires:	json-glib-devel
BuildRequires:	libgcrypt-devel >= 1.1.42
BuildRequires:	libsecret-devel
BuildRequires:	libsoup-devel >= 2.24.0
BuildRequires:	libtool >= 2:2.2.6
BuildRequires:	libxml2-devel >= 1:2.6.26
BuildRequires:	libxslt-devel >= 1.1.17
%{?with_mdb:BuildRequires:	mdbtools-devel >= 0.6-0.pre1.7}
BuildRequires:	meson >= 0.49
%{?with_mysql:BuildRequires:	mysql-devel}
%{?with_ldap:BuildRequires:	openldap-devel}
BuildRequires:	openssl-devel
%{?with_oci:BuildRequires:	oracle-instantclient-devel}
BuildRequires:	perl-base
BuildRequires:	pkgconfig >= 1:0.18
%{?with_pgsql:BuildRequires:	postgresql-devel}
BuildRequires:	python3 >= 1:3
BuildRequires:	readline-devel >= 5.0
BuildRequires:	rpmbuild(macros) >= 1.752
%{?with_sqlcipher:BuildRequires:	sqlcipher-devel >= 3.4}
BuildRequires:	sqlite3-devel >= 3.10.2
BuildRequires:	tar >= 1:1.22
%{?with_vala:BuildRequires:	vala >= 2:0.26.0}
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires:	glib2 >= 1:2.32.0
Conflicts:	libgda4 < 4.2.10-2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		filterout_cpp	-DNDEBUG

%description
GNU Data Access is an attempt to provide uniform access to different
kinds of data sources (databases, information servers, mail spools,
etc). It is a complete architecture that provides all you need to
access your data.

libgda was part of the GNOME-DB project but has been separated from it
to allow non-GNOME applications to be developed based on it.

%description -l pl.UTF-8
GNU Data Access to próba zapewnienia jednolitego dostępu do różnych
źródeł danych (bazy danych, serwery informacji, katalogi z pocztą
itp.). Jest kompletną architekturą dostarczającą wszystko, czego
potrzebujesz do dostępu do danych.

libgda była częścią projektu GNOME-DB, ale została wydzielona, aby
pozwolić na używanie przez niegnomowe aplikacje.

%package devel
Summary:	GNU Data Access development files
Summary(pl.UTF-8):	Pliki programistyczne biblioteki GNU Data Access
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.32.0
Requires:	libxml2-devel >= 1:2.6.26
Requires:	libxslt-devel >= 1.1.17

%description devel
GNU Data Access is an attempt to provide uniform access to different
kinds of data sources (databases, information servers, mail spools,
etc). It is a complete architecture that provides all you need to
access your data. This subpackage contains development files.

%description devel -l pl.UTF-8
GNU Data Access to próba zapewnienia jednolitego dostępu do różnych
źródeł danych (bazy danych, serwery informacji, katalogi z pocztą
itp.). Jest kompletną architekturą dostarczającą wszystko, czego
potrzebujesz do dostępu do danych. Ten podpakiet zawiera pliki dla
programistów używających libgda.

%package static
Summary:	GNU Data Access static libraries
Summary(pl.UTF-8):	Statyczne biblioteki GNU Data Access
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
GNU Data Access static libraries.

%description static -l pl.UTF-8
Statyczne biblioteki GNU Data Access.

%package -n vala-libgda6
Summary:	libgda 6.x API for Vala language
Summary(pl.UTF-8):	API libgda 6.x dla języka Vala
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	vala >= 2:0.26.0
BuildArch:	noarch

%description -n vala-libgda6
libgda 6.x API for Vala language.

%description -n vala-libgda6 -l pl.UTF-8
API libgda 6.x dla języka Vala.

%package ui
Summary:	GNU Data Access UI library
Summary(pl.UTF-8):	Biblioteka GNU Data Access UI
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gtk+3 >= 3.0.0
Requires:	iso-codes

%description ui
GNU Data Access UI library.

%description ui -l pl.UTF-8
Biblioteka GNU Data Access UI.

%package ui-devel
Summary:	Development files for GNU Data Access UI library
Summary(pl.UTF-8):	Pliki programistyczne biblioteki GNU Data Access UI
Group:		Development/Libraries
Requires:	%{name}-ui = %{version}-%{release}
Requires:	gtk+3-devel >= 3.0.0

%description ui-devel
Development files for GNU Data Access UI library.

%description ui-devel -l pl.UTF-8
Pliki programistyczne biblioteki GNU Data Access UI.

%package ui-static
Summary:	GNU Data Access UI static library
Summary(pl.UTF-8):	Statyczna biblioteka GNU Data Access UI
Group:		Development/Libraries
Requires:	%{name}-ui-devel = %{version}-%{release}

%description ui-static
GNU Data Access UI static library.

%description ui-static -l pl.UTF-8
Statyczna biblioteka GNU Data Access UI.

%package -n vala-libgda6-ui
Summary:	libgda-ui 6.x API for Vala language
Summary(pl.UTF-8):	API libgda-ui 6.x dla języka Vala
Group:		Development/Libraries
Requires:	%{name}-ui-devel = %{version}-%{release}
Requires:	vala-libgda6 = %{version}-%{release}

%description -n vala-libgda6-ui
libgda-ui 6.x API for Vala language.

%description -n vala-libgda6-ui -l pl.UTF-8
API libgda-ui 6.x dla języka Vala.

%package apidocs
Summary:	GNU Data Access API documentation
Summary(pl.UTF-8):	Dokumentacja API GNU Data Access
Group:		Documentation
Requires:	gtk-doc-common
BuildArch:	noarch

%description apidocs
GNU Data Access API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API GNU Data Access.

%package provider-db
Summary:	GDA Berkeley DB provider
Summary(pl.UTF-8):	Źródło danych Berkeley DB dla GDA
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description provider-db
This package contains the GDA Berkeley DB provider.

%description provider-db -l pl.UTF-8
Pakiet dostarczający dane z Berkeley DB dla GDA.

%package provider-dbsql
Summary:	GDA Berkeley DB SQL provider
Summary(pl.UTF-8):	Źródło danych Berkeley DB SQL dla GDA
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description provider-dbsql
This package contains the GDA Berkeley DB SQL provider.

%description provider-dbsql -l pl.UTF-8
Pakiet dostarczający dane z Berkeley DB SQL dla GDA.

%package provider-firebird
Summary:	GDA Firebird providers
Summary(pl.UTF-8):	Źródła danych Firebirda dla GDA
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description provider-firebird
This package contains the GDA Firebird providers.

%description provider-firebird -l pl.UTF-8
Pakiet dostarczający dane z Firebirda dla GDA.

%package provider-jdbc
Summary:	GDA JDBC provider
Summary(pl.UTF-8):	Źródło danych JDBC dla GDA
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description provider-jdbc
This package contains the GDA JDBC provider.

%description provider-jdbc -l pl.UTF-8
Pakiet dostarczający dane z JDBC dla GDA.

%package provider-ldap
Summary:	GDA LDAP provider
Summary(pl.UTF-8):	Źródło danych LDAP
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description provider-ldap
This package contains the GDA LDAP provider.

%description provider-ldap -l pl.UTF-8
Pakiet dostarczający dane z LDAP dla GDA.

%package provider-mdb
Summary:	GDA MDB provider
Summary(pl.UTF-8):	Źródło danych MDB
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	mdbtools-libs >= 0.6

%description provider-mdb
This package contains the GDA MDB provider.

%description provider-mdb -l pl.UTF-8
Pakiet dostarczający dane z MDB dla GDA.

%package provider-mysql
Summary:	GDA MySQL provider
Summary(pl.UTF-8):	Źródło danych MySQL dla GDA
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description provider-mysql
This package contains the GDA MySQL provider.

%description provider-mysql -l pl.UTF-8
Pakiet dostarczający dane z MySQL dla GDA.

%package provider-oracle
Summary:	GDA Oracle provider
Summary(pl.UTF-8):	Źródło danych Oracle dla GDA
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description provider-oracle
This package contains the GDA Oracle provider.

%description provider-oracle -l pl.UTF-8
Pakiet dostarczający dane z bazy Oracle dla GDA.

%package provider-postgres
Summary:	GDA PostgreSQL provider
Summary(pl.UTF-8):	Źródło danych PostgreSQL dla GDA
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description provider-postgres
This package contains the GDA PostgreSQL provider.

%description provider-postgres -l pl.UTF-8
Pakiet dostarczający dane z PostgreSQL dla GDA.

%package provider-sqlcipher
Summary:	GDA SQLCipher provider
Summary(pl.UTF-8):	Źródło danych SQLCipher dla GDA
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description provider-sqlcipher
This package contains the GDA SQLCipher provider.

%description provider-sqlcipher -l pl.UTF-8
Pakiet dostarczający dane z SQLCipher dla GDA.

%package provider-sqlite
Summary:	GDA SQLite provider
Summary(pl.UTF-8):	Źródło danych SQLite dla GDA
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	sqlite3 >= 3.10.2

%description provider-sqlite
This package contains the GDA SQLite provider.

%description provider-sqlite -l pl.UTF-8
Pakiet dostarczający dane z SQLite dla GDA.

%package provider-web
Summary:	GDA Web provider
Summary(pl.UTF-8):	Źródło danych Web dla GDA
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description provider-web
This package contains the GDA Web provider.

%description provider-web -l pl.UTF-8
Pakiet dostarczający dane z Web dla GDA.

%package tools
Summary:	Graphical tools for GDA
Summary(pl.UTF-8):	Narzędzia graficzne dla GDA
Group:		X11/Applications
Requires:	%{name}-ui = %{version}-%{release}
Requires:	gtk-update-icon-cache
Requires:	hicolor-icon-theme

%description tools
Graphical tools for GDA.

%description tools -l pl.UTF-8
Narzędzia graficzne dla GDA.

%package glade
Summary:	libgda catalog file and icons for Glade
Summary(pl.UTF-8):	Plik katalogu oraz ikony libgda dla Glade
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	glade >= 3

%description glade
libgda catalog file and icons for Glade.

%description glade -l pl.UTF-8
Plik katalogu oraz ikony libgda dla Glade.

%prep
%setup -q -n libgda-%{version}
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1

%{__sed} -i -e '1s,/usr/bin/env python3,%{__python3},' \
	libgda-report/RML/trml2html/trml2html.py \
	libgda-report/RML/trml2pdf/trml2pdf.py

%build
%meson \
	-Dexperimental=true \
	-Dgraphviz=true \
	-Dlibsecret=true \
	-Dtools=true \
	-Ddoc=true \
	%{?with_ldap:-Dldap=true} \
	-Dweb=true

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

%py3_comp $RPM_BUILD_ROOT%{_datadir}/libgda-6.0/gda_trml2html
%py3_comp $RPM_BUILD_ROOT%{_datadir}/libgda-6.0/gda_trml2pdf
%py3_ocomp $RPM_BUILD_ROOT%{_datadir}/libgda-6.0/gda_trml2html
%py3_ocomp $RPM_BUILD_ROOT%{_datadir}/libgda-6.0/gda_trml2pdf

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libgda-6.0/*/*.a

%{__mv} $RPM_BUILD_ROOT%{_mandir}/man1/{gda-sql,gda-sql-6.0}.1

%find_lang libgda-6.0

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	ui -p /sbin/ldconfig
%postun	ui -p /sbin/ldconfig

%post tools
%update_icon_cache hicolor

%postun tools
%update_icon_cache hicolor

%files -f libgda-6.0.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/gda-list-config-6.0
%attr(755,root,root) %{_bindir}/gda-list-server-op-6.0
%attr(755,root,root) %{_bindir}/gda-sql-6.0
%attr(755,root,root) %{_bindir}/trml2html.py
%attr(755,root,root) %{_bindir}/trml2pdf.py
%attr(755,root,root) %{_libdir}/libgda-6.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgda-6.0.so.6
%attr(755,root,root) %{_libdir}/libgda-report-6.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgda-report-6.0.so.6
%attr(755,root,root) %{_libdir}/libgda-xslt-6.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgda-xslt-6.0.so.6
%{_libdir}/girepository-1.0/Gda-6.0.typelib
%dir %{_libdir}/libgda-6.0
%dir %{_libdir}/libgda-6.0/providers
%dir %{_datadir}/libgda-6.0
# FIXME: examples
%{_datadir}/libgda-6.0/demo
%{_datadir}/libgda-6.0/dtd
%{_datadir}/libgda-6.0/gda-sql
%{_datadir}/libgda-6.0/information_schema.xml
# used by libgda-report
%{_datadir}/libgda-6.0/gda_trml2html
%{_datadir}/libgda-6.0/gda_trml2pdf
%{_mandir}/man1/gda-sql-6.0.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgda-6.0.so
%attr(755,root,root) %{_libdir}/libgda-report-6.0.so
%attr(755,root,root) %{_libdir}/libgda-xslt-6.0.so
%{_datadir}/gir-1.0/Gda-6.0.gir
%dir %{_includedir}/libgda-6.0
%{_includedir}/libgda-6.0/libgda
%{_includedir}/libgda-6.0/libgda-report
%{_includedir}/libgda-6.0/providers
%{_pkgconfigdir}/libgda-6.0.pc
%{_pkgconfigdir}/libgda-capi-6.0.pc
%{_pkgconfigdir}/libgda-models-6.0.pc
%{_pkgconfigdir}/libgda-report-6.0.pc
%{_pkgconfigdir}/libgda-xslt-6.0.pc
# providers
%{?with_db:%{_pkgconfigdir}/libgda-bdb-6.0.pc}
%{?with_dbsql:%{_pkgconfigdir}/libgda-bdbsql-6.0.pc}
%{?with_firebird:%{_pkgconfigdir}/libgda-firebird-6.0.pc}
%{?with_jdbc:%{_pkgconfigdir}/libgda-jdbc-6.0.pc}
%{?with_ldap:%{_pkgconfigdir}/libgda-ldap-6.0.pc}
%{?with_mdb:%{_pkgconfigdir}/libgda-mdb-6.0.pc}
%{?with_mysql:%{_pkgconfigdir}/libgda-mysql-6.0.pc}
%{?with_oci:%{_pkgconfigdir}/libgda-oracle-6.0.pc}
%{?with_pgsql:%{_pkgconfigdir}/libgda-postgres-6.0.pc}
%{?with_sqlcipher:%{_pkgconfigdir}/libgda-sqlcipher-6.0.pc}
%{_pkgconfigdir}/libgda-sqlite-6.0.pc
%{_pkgconfigdir}/libgda-web-6.0.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libgda-6.0.a
%{_libdir}/libgda-report-6.0.a
%{_libdir}/libgda-xslt-6.0.a
%endif

%if %{with vala}
%files -n vala-libgda6
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/libgda-6.0.deps
%{_datadir}/vala/vapi/libgda-6.0.vapi
%endif

%files ui
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/org.gnome.gda.Demoui
%attr(755,root,root) %{_libdir}/libgda-ui-6.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgda-ui-6.0.so.6
%attr(755,root,root) %{_libdir}/libgda-6.0/plugins/libgda-ui-plugins-libgda-6.0.so
%dir %{_libdir}/libgda-6.0/plugins
%{_libdir}/girepository-1.0/Gdaui-6.0.typelib
%{_datadir}/libgda-6.0/ui

%files ui-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgda-ui-6.0.so
%{_includedir}/libgda-6.0/libgda-ui
%{_datadir}/gir-1.0/Gdaui-6.0.gir
%{_pkgconfigdir}/libgda-ui-6.0.pc

%if %{with static_libs}
%files ui-static
%defattr(644,root,root,755)
%{_libdir}/libgda-ui-6.0.a
%endif

%if %{with vala}
%files -n vala-libgda6-ui
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/libgdaui-6.0.vapi
%endif

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libgda-6.0
%{_gtkdocdir}/libgdaui-6.0
%{_datadir}/devhelp/books/Gda-6.0
%{_datadir}/devhelp/books/Gdaui-6.0
%endif

%if %{with db}
%files provider-db
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgda-6.0/providers/libgda-bdb-6.0.so
%endif

%if %{with dbsql}
%files provider-dbsql
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgda-6.0/providers/libgda-bdbsql-6.0.so
%endif

%if %{with firebird}
%files provider-firebird
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgda-6.0/providers/libgda-firebird-client-6.0.so
%endif

%if %{with jdbc}
%files provider-jdbc
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gda-list-jdbc-providers-6.0
%attr(755,root,root) %{_libdir}/libgda-6.0/providers/libgda-jdbc-6.0.so
%{_libdir}/libgda-6.0/providers/gdaprovider-6.0.jar
%endif

%if %{with ldap}
%files provider-ldap
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgda-6.0/providers/libgda-ldap-6.0.so
%endif

%if %{with mdb}
%files provider-mdb
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgda-6.0/providers/libgda-mdb-6.0.so
%endif

%if %{with mysql}
%files provider-mysql
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgda-6.0/providers/libgda-mysql-6.0.so
%endif

%if %{with oci}
%files provider-oracle
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgda-6.0/providers/libgda-oracle-6.0.so
%endif

%if %{with pgsql}
%files provider-postgres
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgda-6.0/providers/libgda-postgres-6.0.so
%endif

%if %{with sqlcipher}
%files provider-sqlcipher
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgda-6.0/providers/libgda-sqlcipher-6.0.so
%endif

%files provider-sqlite
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgda-6.0/providers/libgda-sqlite-6.0.so

%files provider-web
%defattr(644,root,root,755)
%doc providers/web/README
%attr(755,root,root) %{_libdir}/libgda-6.0/providers/libgda-web-6.0.so

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/org.gnome.gda.Browser
%attr(755,root,root) %{_bindir}/gda-control-center-6.0
%{_datadir}/metainfo/org.gnome.gda.Browser.appdata.xml
%{_desktopdir}/org.gnome.gda.Browser.desktop
%{_pixmapsdir}/org.gnome.gda.Browser.png
%{_iconsdir}/hicolor/512x512/apps/org.gnome.gda.Browser.png
%{_iconsdir}/hicolor/scalable/apps/org.gnome.gda.Browser.svg

%if %{with glade}
%files glade
%defattr(644,root,root,755)
%{_datadir}/glade/catalogs/gdaui-catalog.xml
%{_datadir}/glade/pixmaps/widget-gdaui-gdauibasicform.png
%{_datadir}/glade/pixmaps/widget-gdaui-gdauicombo.png
%{_datadir}/glade/pixmaps/widget-gdaui-gdauigrid.png
%{_datadir}/glade/pixmaps/widget-gdaui-gdauilogin.png
%{_datadir}/glade/pixmaps/widget-gdaui-gdauirawgrid.png
%endif
