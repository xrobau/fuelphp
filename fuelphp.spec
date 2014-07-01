Name:		fuelphp
Version:	1.7.1
Release:	1%{?dist}
Summary:	FuelPHP is a simple PHP 5.3 framework
Packager:	Rob Thomas <xrobau@gmail.com>

Group:		Applications/Internet
License:	MIT
URL:		http://fuelphp.com
Source:	http://fuelphp.com/files/download/26#/%{name}-%{version}.zip

Patch:		01-fixsshkeyauth.patch
BuildArch:	noarch

%description
FuelPHP is a simple, flexible, community driven PHP 5.3+ framework, based on the best ideas of other frameworks, with a fresh start!

%prep
%setup -q
%patch

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/fuelphp
for dir in app core packages vendor; do
  dest=%{buildroot}/usr/share/fuelphp/$dir
  mv %{_builddir}/%{name}-%{version}/fuel/$dir $dest
done

%files
/usr/share/fuelphp/*
%doc

%changelog

