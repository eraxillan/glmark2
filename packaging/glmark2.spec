Name: glmark2
Summary: glmark2 is an OpenGL 2.0 and ES 2.0 benchmark (Tizen fork)
Version: 0.0.1
Release: 0
Group: test
License: MIT
Source0: %{name}-%{version}.tar.gz
Source1001: %{name}.manifest

BuildRequires:  ninja
BuildRequires:  gettext-tools
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  python
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-egl)


%description
glmark2 is an OpenGL 2.0 and ES 2.0 benchmark.
glmark2 is developed by Alexandros Frantzis and Jesse Barker based on the
original glmark benchmark by Ben Smith.

%prep
%setup -q -n %{name}-%{version}
cp %{SOURCE1001} .

%build
./waf configure --with-flavors=drm-glesv2,wayland-glesv2
./waf

%install
./waf install --destdir=%{buildroot}

%files
%defattr(-,root,root,-)
%manifest %{name}.manifest
/usr/local/bin/glmark2-es2-wayland
/usr/local/bin/glmark2-es2-drm
/usr/local/share/glmark2/models/*
/usr/local/share/glmark2/shaders/*
/usr/local/share/glmark2/textures/*
/usr/local/share/man/*
