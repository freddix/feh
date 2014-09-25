Summary:	Fast image viewer/indexer/montager
Name:		feh
Version:	2.12
Release:	1
License:	BSD
Group:		X11/Applications/Graphics
Source0:	http://feh.finalrewind.org/%{name}-%{version}.tar.bz2
# Source0-md5:	da59074c2e7b68fb08f555e366f827a9
URL:		http://feh.finalrewind.org/
BuildRequires:	curl-devel
BuildRequires:	giblib-devel
BuildRequires:	imlib2-devel
BuildRequires:	libexif-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	xorg-libXinerama-devel
BuildRequires:	xorg-libXt-devel
Requires(post,postun):	/usr/bin/gtk-update-icon-cache
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	hicolor-icon-theme
Requires:	imlib2-loaders
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
feh is a fast, lightweight image viewer which uses imlib2.

%prep
%setup -q
%{__sed} -i "s,CFLAGS ?=.*,CFLAGS = %{rpmcflags}," config.mk
%{__sed} -i "s,Icon.*,Icon=feh," share/applications/feh.pre

%build
%{__make} \
	CC="%{__cc}"		\
	PREFIX=%{_prefix}	\
	exif=1 help=1 stat64=1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_iconsdir}/hicolor/{48x48,scalable}/apps

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=%{_prefix}

install share/images/feh.png \
	$RPM_BUILD_ROOT%{_iconsdir}/hicolor/48x48/apps
install share/images/feh.svg \
	$RPM_BUILD_ROOT%{_iconsdir}/hicolor/scalable/apps

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor
%update_desktop_database

%postun
%update_icon_cache hicolor
%update_desktop_database

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog examples README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/feh
%{_desktopdir}/feh.desktop
%{_iconsdir}/hicolor/*/apps/*.*
%{_mandir}/man1/*.1*

