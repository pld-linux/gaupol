Summary:	Subtitle editor for text-based subtitles
Summary(pl.UTF-8):	Edytor tekstowych podpisów dla filmów
Name:		gaupol
Version:	0.8
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	http://download.gna.org/gaupol/0.8/%{name}-%{version}.tar.gz
# Source0-md5:	2506a06a7e53ae216fd54915d6932fb2
URL:		http://home.gna.org/gaupol/
BuildRequires:	gettext-devel
BuildRequires:	intltool
BuildRequires:	python-devel >= 1:2.5
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

%description -l pl.UTF-8
Gaupol jest edytorem tekstowych podpisów dla filmów. Jest jeszcze w
początkowej fazie rozwoju i nie zawiera żadnych zaawansowanych opcji.
Zamiarem jest stworzenie prostego, ale potężnego edytora podpisów dla
wielu formatów podpisów. Aktualnie Gaupol jest użyteczny do konwersji
między formatami, tłumaczeń i ręcznego modyfikowania.

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
%{_datadir}/%{name}
%{py_sitescriptdir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}*
%{_mandir}/man1/%{name}*
%{py_sitescriptdir}/%{name}*.egg-info
