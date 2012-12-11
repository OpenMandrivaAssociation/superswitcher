%define name	superswitcher
%define version 0.6
%define release %mkrel 1

Summary:	Featureful window switcher
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{name}-%{version}.tar.gz
License:	GPLv2
Group:		Graphical desktop/Other
Url:		http://superswitcher.googlecode.com/
BuildRequires:	perl-XML-Parser
BuildRequires:	pkgconfig(libwnck-1.0)
BuildRequires:	pkgconfig(gtk+-2.0)
Patch0:		superswitcher-0.6-glib-single-include.patch
Patch1:		superswitcher-0.6-wnck-workspace.patch

%description
SuperSwitcher is a (more feature-ful) replacement for the Alt-Tab window
switching behavior and Ctrl-Alt-Left/Right/Up/Down workspace switching behavior
that is currently provided by Metacity.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%configure2_5x
# GDK_DISPLAY deprecated
pushd src
for f in *; do sed -i 's/gdk_display/GDK_DISPLAY_XDISPLAY (gdk_display_get_default ())/g' "$f" ; done
popd
%make

%install
%makeinstall
%__rm -rf %{buildroot}%{_datadir}/locale

%files
%doc AUTHORS ChangeLog COPYING README TODO
%{_bindir}/%{name}
%{_datadir}/dbus-1/services/%{name}.*
