Name:		fuelphp
Version:	1.7.2
Release:	2
Summary:	FuelPHP is a simple PHP 5.3 framework
Packager:	Rob Thomas <xrobau@gmail.com>

Group:		Applications/Internet
License:	MIT
URL:		http://fuelphp.com

BuildArch:	noarch

Source:	http://fuelphp.com/files/download/28#/%{name}-%{version}.zip

Patch0: 0001-This-appears-to-fix-the-encrypt-decrypt-issues-with-.patch

%description
FuelPHP is a simple, flexible, community driven PHP 5.3+ framework, based on the best ideas of other frameworks, with a fresh start!

%prep
%setup
%patch0 -p1

%install

# Upgrade phpseclib from the 1.8 branch
#rm -rf %{_builddir}/%{name}-%{version}/fuel/core/vendor/phpseclib
#mv %{_builddir}/core-%{commit}/vendor/phpseclib %{_builddir}/%{name}-%{version}/fuel/core/vendor/phpseclib

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
