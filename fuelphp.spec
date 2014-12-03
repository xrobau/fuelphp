Name:		fuelphp
Version:	1.7.2
Release:	4
Summary:	FuelPHP is a simple PHP 5.3 framework
Packager:	Rob Thomas <xrobau@gmail.com>

Group:		Applications/Internet
License:	MIT
URL:		http://fuelphp.com

BuildArch:	noarch

Source0:	http://fuelphp.com/files/download/28#/%{name}-%{version}.zip
Source1:	https://github.com/xrobau/core/archive/%{commit}.tar.gz

Patch0:		0001-Register-force_login-so-it-can-be-logged-out.patch

%global commit 7ff78cbbbe00ff10262b25d612dec039111dfaa2
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%description
FuelPHP is a simple, flexible, community driven PHP 5.3+ framework, based on the best ideas of other frameworks, with a fresh start!

%prep
%setup -b1
cd fuel/packages/auth
%patch0 -p1

%install

# Upgrade phpseclib from rob's branch
rm -rf %{_builddir}/%{name}-%{version}/fuel/core/vendor/phpseclib
mv %{_builddir}/core-%{commit}/vendor/phpseclib %{_builddir}/%{name}-%{version}/fuel/core/vendor/phpseclib

# Now move everything into the dest directories
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
* Fri Jul 04 2014 - Rob Thomas <rob.thomas@schmoozecom.com>
- Upgrade phpseclib from pending pull request
* Wed Jul 02 2014 - Rob Thomas <rob.thomas@schmoozecom.com>
- Initial release
