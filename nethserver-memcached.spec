Summary: NethServer memcached configuration
Name: nethserver-memcached
Version: 1.2.0
Release: 1%{?dist}
License: GPL
URL: %{url_prefix}/%{name} 
Source0: %{name}-%{version}.tar.gz
BuildArch: noarch

Requires: nethserver-base
Requires: memcached

BuildRequires: nethserver-devtools 

%description
NethServer memcached configuration

%prep
%setup

%build
perl createlinks

%install
rm -rf $RPM_BUILD_ROOT
(cd root; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
%{genfilelist} $RPM_BUILD_ROOT > %{name}-%{version}-filelist

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)
%doc COPYING
%dir %{_nseventsdir}/%{name}-update

%changelog
* Thu Apr 08 2021 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.2.0-1
- Memcached: Listen only to localhost - NethServer/dev#6473

* Thu Jul 07 2016 Stefano Fancello <stefano.fancello@nethesis.it> - 1.1.0-1
- First NS7 release

* Wed Feb 05 2014 Davide Principi <davide.principi@nethesis.it> - 1.0.2-1.ns6
- Lib: synchronize service status prop and chkconfig - Feature #2067 [NethServer]

* Tue Apr 30 2013 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.1-1.ns6
• Rebuild for automatic package handling. #1870

* Tue Mar 19 2013 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.0-2.ns6
- Update URL in spec

* Thu Jan 31 2013 Davide Principi <davide.principi@nethesis.it> - 1.0.0-1.ns6
- Initial release


