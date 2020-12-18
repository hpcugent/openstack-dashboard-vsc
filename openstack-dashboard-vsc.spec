#
# Copyright 2019 Ghent University
#
# This file is part of openstack-dashboard-vsc,
# originally created by the HPC team of the University of Ghent (http://ugent.be/hpc).
#
#
# https://github.com/hpcugent/openstack-dashboard-vsc
#
# openstack-dashboard-vsc is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation v2.
#
# openstack-dashboard-vsc is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with openstack-dashboard-vsc. If not, see <http://www.gnu.org/licenses/>.
##

%{!?_rel:%{expand:%%global _rel 2}}

%define dashboardpath /usr/share/openstack-dashboard/openstack_dashboard/local
%define dashboardconf /etc/openstack-dashboard/local_settings.d
%define vscpanelpath %{dashboardpath}/vsc
%define localsettings %{dashboardpath}/local_settings.d
%define imagespath /usr/share/openstack-dashboard/openstack_dashboard/themes/default/img

Summary: VSC OpenStack dashboard
Name: openstack-dashboard-vsc
Version: 1.0
Release: 8%{?dist}
License: GPLv2
Group: Applications/System
URL: https://www.vscentrum.be/
Source: %{name}-%{version}.tar.gz
ExclusiveOS: linux
BuildRoot: %{?_tmppath}%{!?_tmppath:/var/tmp}/%{name}-%{version}-%{release}-root
BuildArch: noarch
Requires: openstack-dashboard
Requires: openstack-manila-ui


%description
openstack-dashboard-vsc provides the required OpenStack panels
for VSC Tier1-Cloud projects.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{vscpanelpath}
mkdir -p $RPM_BUILD_ROOT%{localsettings}
mkdir -p $RPM_BUILD_ROOT%{imagespath}
mkdir -p $RPM_BUILD_ROOT%{dashboardconf}

install -m 0644 panels/_00_vsc.py $RPM_BUILD_ROOT%{localsettings}/_00_vsc.py
install -m 0644 panels/_12_vsc_theme.py $RPM_BUILD_ROOT%{dashboardconf}/_12_vsc_theme.py
install -m 0644 panels/__init__.py $RPM_BUILD_ROOT%{vscpanelpath}/__init__.py
install -m 0644 panels/_disabled.py $RPM_BUILD_ROOT%{vscpanelpath}/_disabled.py
install -m 0644 img/favicon.ico $RPM_BUILD_ROOT%{imagespath}/favicon.ico
install -m 0644 img/logo-splash.svg $RPM_BUILD_ROOT%{imagespath}/logo-splash.svg
install -m 0644 img/logo.svg $RPM_BUILD_ROOT%{imagespath}/logo.svg

# Disabled tabs
ln -s _disabled.py $RPM_BUILD_ROOT%{vscpanelpath}/_1360_project_volume_groups.py
ln -s _disabled.py $RPM_BUILD_ROOT%{vscpanelpath}/_1370_project_vg_snapshots.py
ln -s _disabled.py $RPM_BUILD_ROOT%{vscpanelpath}/_1440_project_routers_panel.py
ln -s _disabled.py $RPM_BUILD_ROOT%{vscpanelpath}/_9020_manila_project_add_share_snapshots_panel_to_share_panel_group.py
ln -s _disabled.py $RPM_BUILD_ROOT%{vscpanelpath}/_9040_manila_project_add_share_networks_panel_to_share_panel_group.py
ln -s _disabled.py $RPM_BUILD_ROOT%{vscpanelpath}/_9050_manila_project_add_security_services_panel_to_share_panel_group.py
ln -s _disabled.py $RPM_BUILD_ROOT%{vscpanelpath}/_9080_manila_project_add_share_groups_panel_to_share_panel_group.py
ln -s _disabled.py $RPM_BUILD_ROOT%{vscpanelpath}/_9085_manila_project_add_share_group_snapshots_panel_to_share_panel_group.py

%post

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)

%{localsettings}/_00_vsc.py
%{dashboardconf}/_12_vsc_theme.py
%{vscpanelpath}/__init__.py
%{vscpanelpath}/_disabled.py

%{vscpanelpath}/_1360_project_volume_groups.py
%{vscpanelpath}/_1370_project_vg_snapshots.py
%{vscpanelpath}/_1440_project_routers_panel.py
%{vscpanelpath}/_9020_manila_project_add_share_snapshots_panel_to_share_panel_group.py
%{vscpanelpath}/_9040_manila_project_add_share_networks_panel_to_share_panel_group.py
%{vscpanelpath}/_9050_manila_project_add_security_services_panel_to_share_panel_group.py
%{vscpanelpath}/_9080_manila_project_add_share_groups_panel_to_share_panel_group.py
%{vscpanelpath}/_9085_manila_project_add_share_group_snapshots_panel_to_share_panel_group.py

%{imagespath}/favicon.ico
%{imagespath}/logo-splash.svg
%{imagespath}/logo.svg

%attr(0755, root, root) %dir %{vscpanelpath}
%attr(0755, root, root) %dir %{imagespath}

%changelog
* Thu Feb 7 2019 Álvaro Simón <Alvaro.SimonGarcia@UGent.be>
- Initial build.
