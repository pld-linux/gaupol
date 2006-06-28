Summary:	Subtitle editor for text-based subtitles
Summary(pl):	Edytor tekstowych podpisów dla filmów
Name:		gaupol
Version:	0.5.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://download.gna.org/gaupol/0.5/%{name}-%{version}.tar.gz
# Source0-md5:	6b4386c76c1756b035306c0b5c179602
URL:		http://home.gna.org/gaupol/
BuildRequires:	gettext-devel
BuildRequires:	intltool
BuildRequires:	python-devel >= 1:2.4
BuildRequires:	rpm-pythonprov
Requires:	python-pygtk-glade >= 2:2.8.0
%pyrequires_eq	python-modules
#Suggests:	python-pyenchant >= 1.1.3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gaupol is a subtitle editor for text-based subtitles. Gaupol is in
early development stage and does not yet contain any advanced
features. The aim is to make a simple, but powerful, subtitle editor
for multiple subtitle formats. Currently Gaupol is useful for
converting between different formats, translating and manual editing.

%description -l pl
Gaupol jest edytorem tekstowych podpisów dla filmów. Jest jeszcze w
pocz±tkowej fazie rozwoju i nie zawiera ¿adnych zaawansowanych opcji.
Zamiarem jest stworzenie prostego, ale potê¿nego edytora podpisów dla
wielu formatów podpisów. Aktualnie Gaupol jest u¿yteczny do konwersji
miêdzy formatami, t³umaczeñ i rêcznego modyfikowania.

%prep
%setup -q

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--optimize=2 \
	--root $RPM_BUILD_ROOT \
	--prefix %{_prefix}

find $RPM_BUILD_ROOT%{py_sitescriptdir}/gaupol -name '*.py' -exec rm -f {} \;

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/gaupol
%{py_sitescriptdir}/gaupol
%{_desktopdir}/*
%{_iconsdir}/hicolor/*/apps/*
